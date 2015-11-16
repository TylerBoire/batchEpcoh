#!/bin/python

from datetime import datetime
import pytz

timeFile = raw_input("Where is the file located: ") 

with open (timeFile, 'r') as date:
	for line in date:
		tz = pytz.timezone('America/New_York')
		dt = datetime.fromtimestamp((float(line)/1000),tz)
		print(dt.strftime('%Y-%m-%d %H:%M%S %Z%z'))
