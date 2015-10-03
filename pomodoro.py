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
	os.system("echo 'WORK - From %s to %s - %s' >> work_done.txt"%(starttime, endtime, work))
	
	
elif(type == "break"):
	os.system("notify-send 'Starting 5 minutes break.'")
	os.system("cat original.txt > /etc/hosts")
	starttime = str(datetime.datetime.now())
	for i in range(5):
		print 5-i," minutes to go..."
		time.sleep(60)
	endtime = str(datetime.datetime.now())
	os.system("notify-send 'Break time ends.'")
	work = raw_input("What did you do?")
	os.system("echo 'REST - From %s to %s - %s' >> work_done.txt"%(starttime, endtime, work))
		
	
else:
	print "else"