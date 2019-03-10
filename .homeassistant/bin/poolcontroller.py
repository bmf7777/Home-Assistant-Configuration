#!/srv/homeassistant/bin/python

from requests import get
import json
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

http = get(url)
json = json.dumps(xmltodict.parse(http.content), indent=4)
print( json )
exit()





