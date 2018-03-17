#!/usr/bin/env python36

import requests, graphitesend, redis
import json, time

def SendData():
  response = requests.get(URL)

  if response.status_code == 200:
    AllData = response.json()
    new_dict = {}
    sitename = "koinex"
    for crypto in AllData['stats']:
      crypto_name = crypto
      new_key_1 = sitename + '-' + crypto_name.lower() + '-last'
      new_val_1 = AllData['stats'][crypto_name]['last_traded_price']
      new_dict.update({new_key_1:new_val_1})
      new_key_2 = sitename + '-' + crypto_name.lower() + '-buy'
      new_val_2 = AllData['stats'][crypto_name]['highest_bid']
      new_dict.update({new_key_2:new_val_2})
      new_key_3 = sitename + '-' + crypto_name.lower() + '-sell'
      new_val_3 = AllData['stats'][crypto_name]['lowest_ask']
      new_dict.update({new_key_3:new_val_3})
      new_key_4 = sitename + '-' + crypto_name.lower() + '-24h-volume-inr'
      new_val_4 = AllData['stats'][crypto_name]['vol_24hrs']
      new_dict.update({new_key_4:new_val_4})
    g.send_dict(new_dict)
    r.hmset("Koinex", new_dict) 
     
  else:
    pass

if __name__=="__main__":
    
    URL = "https://koinex.in/api/ticker"
    SERVER = '127.0.0.1' 
    CARBON_PORT = 2003
    REDIS_PORT = 6379
    r = redis.Redis(host=SERVER, port=REDIS_PORT, db=0)
    g = graphitesend.init(graphite_server=SERVER, graphite_port=CARBON_PORT, group='metrics-koinex')
  
    while True:
        SendData()
        time.sleep(22)
