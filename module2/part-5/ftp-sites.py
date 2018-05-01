#!/usr/bin/env python
# Got some help from this site - https://hackernoon.com/synchronization-primitives-in-python-564f89fee732
# accessed 25 April 2018

import ftplib
import os

import threading
import Queue
import time

# run in directory of file (not necessary unless called from another directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

ftpsites = [
"ftp.bom.gov.au",
"ftp.ga.gov.au",
"ftp.aao.gov.au",
"neoftp.sci.gsfc.nasa.gov",
"ftp.fu-berlin.de",
"ftp.gnu.org",
"ftp.isi.edu",
"ftp.freebsd.org",
"speedtest.tele2.net",
"ftp.aao.gov.au"
]
port = 21
timeout = 3

print bcolors.HEADER + str(ftpsites) + bcolors.ENDC

def ftpPoke(*args):
	if len(args) < 1:
		print "function ftpPoke received no arguments ... exiting"
		return
	
	hostname = args[0]
	if len(args) > 1:
		port = int(args[1])
	if len(args) > 2:
		timeout = int(args[2])
 

	ftp = ftplib.FTP()
	try:
		ftp.connect(hostname,port,timeout)
		ftp.login()
		lock.acquire()
		print bcolors.HEADER + '%s\n%s'%(hostname,len(hostname)*'-') + bcolors.ENDC
		ftp.dir()
		ftp.quit()
		lock.release()	
	except Exception as im:
		print bcolors.FAIL + '%s\n'%(hostname) + str(im) + bcolors.ENDC

#ftpPoke(hostname, port, timeout)

class WorkerThread(threading.Thread):
	
	# Note - lock is a class variable accessible to all the threads
	# see https://stackoverflow.com/questions/33227423/any-suggestions-on-why-the-lock-mechanism-isnt-getting-implemented-in-the-below
	# accessed 25 April 2018
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		print "In Worker Thread"
		while True:
			hostname = self.queue.get()
##			print "hostname = %s"%hostname
			ftpPoke(hostname, port, timeout)
			print "%s finished"%(self.getName())
			self.queue.task_done()


queue = Queue.Queue()
lock = threading.Lock()

for i in range(5):
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "%s created!"%(worker.getName())

counter = 0 
for site in ftpsites:
	print bcolors.HEADER + "%d. site %s"%(counter,site) + bcolors.ENDC
	counter += 1
	queue.put(site)


try:
	queue.join()
except Exception as im:
	print bcolors.FAIL + str(im) + bcolors.ENDC
	

print "All tasks are over"
