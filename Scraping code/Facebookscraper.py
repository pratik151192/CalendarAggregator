import facebook
import json
import datetime
import csv
import time
import requests
from pprint import pprint
import unicodedata

#connecting to FB graph API
APP_ID = '1842196376027654'
APP_SECRET = '80b12310850e1131a523910c02b91e61'
graph = facebook.GraphAPI(APP_ID + "|" + APP_SECRET)

#setting up initial/basic query
to_scrape_lists = ["ISTatPENNSTATE"]
query = "/events"
list=[]
def getEventData(incoming_post):
	new_query = incoming_post + query
	events = graph.get_object(new_query)
	i=0
	for i in range(0,26):
		try:
			list1={}
			list1["id"] = i
			list1["title"] = events["data"][i]["name"]
			list1["start"]= (events["data"][i]["start_time"])[0:10]
			try:
				list1["end"] = (events["data"][i]["end_time"])[0:10]
			except KeyError:
				list1["end"] = ""
			#list1["url"] = "events.html#" + str(i)
			list1["desc"] = events["data"][i]["description"]
			try:
				list1["location"] = events["data"][i]["place"]["name"]
			except KeyError:
				list1["location"] = ""
			list.append(list1)
		except IndexError:
			break
		except KeyError:
			continue

for l in range(0, len(to_scrape_lists)):
	getEventData(to_scrape_lists[l])
a=json.dumps(list)
with open("facebook.json","w") as file1:
	json.dump(list,file1)
'''with open("facebook.csv","w") as file1:
	writer = csv.writer(file1)'''
	
	

