#!/usr/bin/python3

import requests,json,ast,time,graphitesend


URL="https://koinex.in/api/ticker"
CARBON_SERVER = '127.0.0.1' 
CARBON_PORT = 2003
g = graphitesend.init(graphite_server='127.0.0.1', graphite_port=2003, group='koinex-graphs')


def SendData():
  response = requests.get(URL)

  if response.status_code == 200:
    AllData = ast.literal_eval(response.content.decode('UTF-8'))
    g.send_dict(
      {
	'KOI-XRP-INR': AllData['prices']['XRP'],
	'KOI-XRP-VOL-24hr': AllData['stats']['XRP']['vol_24hrs'],
      }
  )
     
  else:
    pass

if __name__=="__main__":
  while True:
    time.sleep(20)
    SendData()
