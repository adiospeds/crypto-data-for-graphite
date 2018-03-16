#!/usr/bin/python3

import requests,json,ast,time,graphitesend

URL = "https://coindelta.com/api/v1/public/getticker/"
CARBON_SERVER = '127.0.0.1' 
CARBON_PORT = 2003
g = graphitesend.init(graphite_server='127.0.0.1', graphite_port=2003, group='coindelta-graphs')

def SendData():
  response = requests.get(URL)

  if response.status_code == 200:
    AllData = ast.literal_eval(response.content.decode('UTF-8'))
    g.send_dict(
      {
	'BTCINR' : AllData[0]['Last'],
	'ETHINR' : AllData[1]['Last'],
	'LTCINR' : AllData[2]['Last'],
	'OMGINR' : AllData[3]['Last'],
	'QTUMINR' : AllData[4]['Last'],
	'XRPINR' : AllData[9]['Last'],
	'BCHINR' : AllData[11]['Last'],
	'ETHBTC' : AllData[5]['Last'],
	'LTCBTC' : AllData[6]['Last'],
	'OMGBTC' : AllData[7]['Last'],
	'QTUMBTC' : AllData[8]['Last'],
	'XRPBTC' : AllData[10]['Last']
      }
  )
     
  else:
    pass

if __name__=="__main__":
  while True:
    time.sleep(2)
    SendData()
    print("X")
