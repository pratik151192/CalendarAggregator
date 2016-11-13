import time
import datetime

import codecs
import json
import urllib
from urllib import request
from markupsafe import Markup

#from future.standard_library import install_aliases
#install_aliases()

from urllib.parse import urlparse, urlencode

with open('data.json', 'r') as data_file:    
    data = json.load(data_file)

reader = codecs.getreader('utf-8')
a = json.load(reader(request.urlopen("https://apidev.accuweather.com/forecasts/v1/daily/10day/335315?apikey=PSUHackathon112016")))

for event in data: # add search query for embed
	event['query'] = urlencode({"q": event['location']})

from jinja2 import Template
dates = {}
icon = {}

for i in range(0,10):
	text = a["DailyForecasts"][i]["Date"][0:10]
	dates[text] = a["DailyForecasts"][i]["Temperature"]
	icon[text] = a["DailyForecasts"][i]["Day"]

with open('event-temp.html', 'r') as temp_file: 
    template = Template(temp_file.read())

with open("events.html","w") as output:
	output.write(template.render(data=data, dates=dates, icon=icon ))