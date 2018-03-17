#!/usr/bin/env python36

import requests, graphitesend, redis
import json, time


def SendData():
  response = requests.get(URL)
  if response.status_code == 200:
    AllData = response.json()
    new_dict = {}
    sitename = "cmc"
    for i in AllData:
      if i['id'] in cryptos:
        new_key_1 = sitename + '-' + i['symbol'].lower() + '-last'
        new_val_1 = i['price_inr']
        new_dict.update({new_key_1:new_val_1})
        new_key_2 = sitename + '-' + i['symbol'].lower() + '-usd'
        new_val_2 = i['price_inr']
        new_dict.update({new_key_2:new_val_2})
        new_key_3 = sitename + '-' + i['symbol'].lower() + '-24h-pct-change'
        new_val_3 = i['percent_change_24h']
        new_dict.update({new_key_3:new_val_3})
        new_key_4 = sitename + '-' + i['symbol'].lower() + '-24h-volume-usd'
        new_val_4 = i['24h_volume_usd']
        new_dict.update({new_key_4:new_val_4})
        new_key_5 = sitename + '-' + i['symbol'].lower() + '-24h-volume-inr'
        new_val_5 = i['24h_volume_inr']
        new_dict.update({new_key_5:new_val_5})
        new_key_6 = sitename + '-' + i['symbol'].lower() + '-rank'
        new_val_6 = i['rank']
        new_dict.update({new_key_6:new_val_6})
    g.send_dict(new_dict)
    r.hmset("Cmc", new_dict)
  else:
    pass

if __name__=="__main__":

  cryptos = ["bitcoin", "ethereum", "ripple", "bitcoin-cash", "litecoin", "cardano", "neo", "stellar", "eos", "monero", "dash", "iota", "nem", "tron", "ethereum-classic", "vechain", "lisk", "nano", "omisego", "qtum", "bitcoin-gold", "zcash", "verge", "dogecoin", "siacoin", "ontology", "aeternity", "0x", "electroneum", "digibyte", "golem-network-tokens", "gas", "basic-attention-token", "zcoin", "deepbrain-chain", "red-pulse", "request-network", "zilla", "ncash", "aion" ]

  URL = "https://api.coinmarketcap.com/v1/ticker/?convert=INR&limit=1000"
  SERVER = '127.0.0.1' 
  CARBON_PORT = 2003
  REDIS_PORT = 6379
  r = redis.Redis(host=SERVER, port=REDIS_PORT, db=0)
  g = graphitesend.init(graphite_server=SERVER, graphite_port=CARBON_PORT, prefix='ohio-analyzer-1.metrics-cmc', system_name='')


  while True:
    time.sleep(6)
    SendData()






