from icalendar import Calendar, Event
import json
import sys
summary = []
bdate = []
edate = []
	
f=open("calendar.ics",'r')
cal = Calendar.from_ical(f.read())
for event in cal.walk():
	if event.name == "VEVENT":
		start = event.get('dtstart')
		end = event.get('dtend')
		summary.append(event.get('summary'))
		bdate.append(start.dt)
		edate.append(end.dt)
list = []

for i in range(0,len(summary)):
	list1={}
	list1["id"] = i+25
	list1["title"] = str(summary[i])
	list1["start"] = str(bdate[i])[0:20]
	list1["end"] = str(edate[i])[0:20]
	list1["desc"] = ""
	list1["location"] = ""	
	#list1["url"] = "events.html#" + str(i+25)
	list.append(list1)
a = json.dumps(list)
outputfile = "calendar.json"
with open(outputfile,"w") as file1:
	json.dump(list,file1)
