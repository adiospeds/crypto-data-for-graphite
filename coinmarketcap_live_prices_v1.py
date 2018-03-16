#!/usr/bin/python3

import requests,json,ast,time,graphitesend


URL="https://api.coinmarketcap.com/v1/ticker/ripple/?convert=INR&limit=10"
CARBON_SERVER = '127.0.0.1' 
CARBON_PORT = 2003
g = graphitesend.init(graphite_server='127.0.0.1', graphite_port=2003, group='cmc-graphs')


def SendData():
  response = requests.get(URL)

  if response.status_code == 200:
    AllData = ast.literal_eval(response.content.decode('UTF-8'))
    g.send_dict(
      {
	'CMC-XRP-INR': AllData[0]['price_inr'],
	'CMC-XRP-USD': AllData[0]['price_usd'], 
      }
  )
     
  else:
    pass

if __name__=="__main__":
  while True:
    time.sleep(6)
    SendData()
