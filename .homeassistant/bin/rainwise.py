#!/srv/homeassistant/bin/python

from bs4 import BeautifulSoup
import urllib3
import json

# Rainwise MK-III weather station address 
url = "http://192.168.1.31"

http = urllib3.PoolManager()
r = http.request('GET', url)
#content = urllib3.urlopen(url).read()
#soup = BeautifulSoup(content, 'lxml')
soup = BeautifulSoup(r.data, 'lxml')
data = {}

data["air_temperature"] = soup.find(id='tic').string
data["relative_humidity"] = soup.find(id='ric').string
data["barometric_pressure"] = soup.find(id='bic').string
data["wind"] = soup.find(id='wic').string
data["rainfall"] = soup.find(id='rfd').string
data["station_battery"] = soup.find(id='batt').string

json_data = json.dumps(data)

print( json_data )

