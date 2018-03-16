#!/usr/bin/python3

import requests,graphitesend,time,json


URL="https://bitbns.com/order/getTickerAll"
CARBON_SERVER = '127.0.0.1' 
CARBON_PORT = 2003
g = graphitesend.init(graphite_server='127.0.0.1', graphite_port=2003, group='bitbns-graphs')



def SendData():
  response = requests.get(URL)
  
  if response.status_code == 200:
    AllData = response.json()
    for data in AllData:
       for each_crypto in data:
         crypto_name = each_crypto
         new_dict = {}
       for key,val in data[crypto_name].items():
         new_key = crypto_name+"-"+key
         new_dict.update({new_key:val})
       print(new_dict)
       g.send_dict(new_dict)
  else:
    pass

if __name__=="__main__":
  while True:
    SendData()
    time.sleep(5)
