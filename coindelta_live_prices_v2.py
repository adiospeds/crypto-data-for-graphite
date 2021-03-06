#!/usr/bin/env python36

import requests, graphitesend, redis
import json, time


def SendData():
    response = requests.get(URL)
    if response.status_code == 200:
        AllData = response.json()
        new_dict = {}
        sitename = "coindelta"
        for data in AllData:
            crypto_name = data['MarketName']
            if '-inr' in crypto_name:
                crypto_name = crypto_name.split('-')[0]
                new_key_1 = sitename + '-' + crypto_name + '-last'
                new_val_1 = data['Last']
                new_dict.update({new_key_1:new_val_1})
                new_key_2 = sitename + '-' + crypto_name + '-buy'
                new_val_2 = data['Bid']
                new_dict.update({new_key_2:new_val_2})
                new_key_3 = sitename + '-' + crypto_name + '-sell'
                new_val_3 = data['Ask']
                new_dict.update({new_key_3:new_val_3})
        g.send_dict(new_dict)
        r.hmset("Coindelta", new_dict)
    else:
        pass

if __name__=="__main__":

    URL = "https://coindelta.com/api/v1/public/getticker/"
    SERVER = '127.0.0.1' 
    CARBON_PORT = 2003
    REDIS_PORT = 6379
    r = redis.Redis(host=SERVER, port=REDIS_PORT, db=0)
    g = graphitesend.init(graphite_server=SERVER, graphite_port=CARBON_PORT, prefix='ohio-analyzer-1.metrics-coindelta', system_name='')

    while True:
        SendData()
        time.sleep(5)
