import sys
import os
import time
if len(sys.argv) > 1:
	type = sys.argv[1]

if type == "work":
	os.system("notify-send 'Starting 25 minutes timer.'")
	os.system("cat original.txt > /etc/hosts")
	os.system("cat block.txt >> /etc/hosts")
	for i in range(25):
		print 25-i," minutes to go..."
		time.sleep(60)
	os.system("notify-send 'Work time ends.'")
	
elif(type == "break"):
	os.system("notify-send 'Starting 5 minutes break.'")
	os.system("cat original.txt > /etc/hosts")
	for i in range(5):
		print 5-i," minutes to go..."
		time.sleep(1)
	os.system("notify-send 'Break time ends.'")
		
	
else:
	print "else"