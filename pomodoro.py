import sys
import os
import time
import datetime
if len(sys.argv) > 1:
	type = sys.argv[1]

if type == "work":
	os.system("notify-send 'Starting 25 minutes timer.'")
	os.system("cat original.txt > /etc/hosts")
	os.system("cat block.txt >> /etc/hosts")
	starttime = str(datetime.datetime.now())
	for i in range(25):
		print 25-i," minutes to go..."
		time.sleep(60)
	endtime = str(datetime.datetime.now())
	os.system("notify-send 'Work time ends.'")
	work = raw_input("What did you do?")
	os.system("echo 'WORK - From %s to %s - %s' >> 4_october_2015.txt"%(starttime, endtime, work))
	
	
elif(type == "break"):
	break_duration = int(raw_input("Break Duration: "))
	# notification = "Starting break for %d minutes"
	os.system("notify-send 'Starting %d minutes break.'"%break_duration)
	os.system("cat original.txt > /etc/hosts")
	starttime = str(datetime.datetime.now())
	for i in range(break_duration):
		print break_duration-i," minutes to go..."
		time.sleep(60)
	endtime = str(datetime.datetime.now())
	os.system("notify-send 'Break time ends.'")
	work = raw_input("What did you do?")
	os.system("echo 'REST - From %s to %s - %s' >> 4_october_2015.txt"%(starttime, endtime, work))
		
elif type == "sleep":
	os.system("notify-send 'Preparing for sleep'")
	os.system("echo 'SLEEP' >> 4_october_2015.txt")
	
else:
	print "else"