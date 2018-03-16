#!/usr/bin/env python3

import requests, graphitesend, redis
import time, json




def SendData():
  response = requests.get(URL)
  
  if response.status_code == 200:
    AllData = response.json()
    sitename = "bitbns"
    new_dict = {}
    for data in AllData:
       for each_crypto in data:
         crypto_name = each_crypto
       for key,val in data[crypto_name].items():
         if 'buyPrice' in key:
           new_key = sitename + '-' + crypto_name.lower() + "-buy"
         elif 'sellPrice' in key:
           new_key = sitename + '-' + crypto_name.lower() + "-sell"
         elif 'lastTradePrice' in key:
           new_key = sitename + '-' + crypto_name.lower() + "-last"
         new_dict.update({new_key:val})
       g.send_dict(new_dict)
       r.hmset("Bitbns", new_dict)
  else:
    pass

if __name__ == "__main__":

  URL="https://bitbns.com/order/getTickerAll"
  SERVER = '127.0.0.1' 
  CARBON_PORT = 2003
  REDIS_PORT = 6379
  r = redis.Redis(host=SERVER, port=REDIS_PORT, db=0)
  g = graphitesend.init(graphite_server=SERVER, graphite_port=CARBON_PORT, group='metrics-bitbns')
  while True:
    SendData()
    time.sleep(5)

