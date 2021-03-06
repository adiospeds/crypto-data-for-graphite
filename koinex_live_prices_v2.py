#!/usr/bin/env python36

import requests, graphitesend, redis
import json, time
#import pdb

def SendData():
  #pdb.set_trace()
  response = requests.get(URL)

  if response.status_code == 200:
    AllData = response.json()
    new_dict = {}
    sitename = "koinex"
    for crypto in AllData['stats']['inr']:
      crypto_name = crypto
      new_key_1 = sitename + '-' + crypto_name.lower() + '-last'
      new_val_1 = AllData['stats']['inr'][crypto_name]['last_traded_price']
      new_dict.update({new_key_1:float(0 if new_val_1 is None else new_val_1)})
      new_key_2 = sitename + '-' + crypto_name.lower() + '-buy'
      new_val_2 = AllData['stats']['inr'][crypto_name]['highest_bid']
      new_dict.update({new_key_2:float(0 if new_val_2 is None else new_val_2)})
      new_key_3 = sitename + '-' + crypto_name.lower() + '-sell'
      new_val_3 = AllData['stats']['inr'][crypto_name]['lowest_ask']
      new_dict.update({new_key_3:float(0 if new_val_3 is None else new_val_3)})
      new_key_4 = sitename + '-' + crypto_name.lower() + '-24h-volume-inr'
      new_val_4 = AllData['stats']['inr'][crypto_name]['vol_24hrs']
      new_dict.update({new_key_4:float(0 if new_val_4 is None else new_val_4)})
    g.send_dict(new_dict)
    r.hmset("Koinex", new_dict) 
     
  else:
    pass ## left for some stuffing here

if __name__=="__main__":
    
    URL = "https://koinex.in/api/ticker"
    SERVER = '127.0.0.1' 
    CARBON_PORT = 2003
    REDIS_PORT = 6379
    r = redis.Redis(host=SERVER, port=REDIS_PORT, db=0)
    g = graphitesend.init(graphite_server=SERVER, graphite_port=CARBON_PORT, prefix='ohio-analyzer-1.metrics-koinex', system_name='')
  
    while True:
        SendData()
        time.sleep(5)
