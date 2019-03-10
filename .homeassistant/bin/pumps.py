#!/srv/homeassistant/bin/python

from requests import get
import json
import untangle
import xmltodict

circuit1 = "SPA"
circuit2 = "BOOSTERPUMP"
circuit3 = "AIR BLOWER"
circuit4 = "POOL LIGHT"
circuit5 = "WATERFALL"
circuit6  = "POOL"
circuit8 = "SPA LIGHT"
feature1 = "FLOOR CLEANER"

url = "http://admin:admin@192.168.1.253/status.xml"
url2 = "http://admin:admin@192.168.1.253/pumps.xml"

http_status = get(url)
http_pumps = get(url2)

status = untangle.parse(http_status.text)
pumps = untangle.parse(http_pumps.text)

vsp_pool_status = status.response.equipment.circuit6.cdata
vsp_spa_status = status.response.equipment.circuit1.cdata
if vsp_pool_status == '0' and vsp_spa_status == '0':
  print("Pump OFF")
else :
  vsp = pumps.response.pumps.pump1.cdata
  vsp = vsp.split(',',3)
  power = vsp[0]
  rpm = vsp[1]
  print (power, "Watts",  rpm, "RPM")





