#!/usr/bin/env python
 
# Module 02, Part 02, Exercise 2
# For any given filename list out all the stats related to the file
# such as size, creation time, path, etc.

import os, time, sys
#path = os.path.join('/home/ubuntu/workspace','pset7.sql') # can get this as an argument?

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

for item in sys.argv[1:]:
	path = item
	print "\n\n" + bcolors.HEADER
	print "path = ",path
	print "--------------------------------------------------------" + bcolors.ENDC
	try:
		print "Current Time = ",time.ctime()
		mystat = os.stat(path)

		print "st_mode - protection bits: {0:20}".format(mystat.st_mode)
		print "st_ino - inode number:     {0:20}".format(mystat.st_ino)
		print "st_dev - device            {0:20}".format(mystat.st_dev)
		print "st_nlink - number of hard links\t\t\t", mystat.st_nlink
		print "st_uid - user id of owner\t\t\t", mystat.st_uid
		print "st_gid - group id of owner\t\t\t", mystat.st_gid
		print "st_size - size of file, in bytes\t\t\t",mystat.st_size
		print "st_atime - time of most recent access\t\t\t",time.ctime(mystat.st_atime)
		print "st_mtime - time of most recent content modification\t\t\t\t",time.ctime(mystat.st_mtime)
		print "st_ctime - platform dependent; time of most recent metadata change on Unix",time.ctime(mystat.st_ctime)
	except Exception as im:
		print bcolors.FAIL + "Exception: " + str(im) + bcolors.ENDC
