#!/bin/python3
import json
import turtle
import urllib.request
from http import client

import gmplot
import py3 as py3
from requests import api



url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
#print (result)
#longitudes = ["Location:", result['iss_position']['longitude'], '/r']
#latitudes = ("Location:", result['iss_position']['latitude'])

longitudes = float(result['iss_position']['longitude'])
latitudes = float(result['iss_position']['latitude'])

gmap = gmplot.GoogleMapPlotter(latitudes, longitudes, 3)
gmap.marker(latitudes, longitudes, color='#FF0000', c='#FF0000')



gmap.draw("mymap.html")