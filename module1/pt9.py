#!/usr/bin/env python

try:
	from bcolors import bcolors 
except:
	print "bcolors not found"

# try-exception blocks

try:
	print "try:\n\ta = 10/20"
	a = 10/20
except:
	print bcolors.FAIL+ "Exception" + bcolors.ENDC
else:
	print bcolors.OKGREEN + "This code runs if no exception" + bcolors.ENDC
finally: 
	print "Finally, Cleanup code This part always runs"	


try:
	print "try:\n\ta=10/0"
	a = 10/0
except:
	print bcolors.FAIL + "Exception" + bcolors.ENDC
else:
	print bcolors.OKGREEN + "This code runs if no exception" + bcolors.ENDC
finally: 
	print "Finally, Cleanup code This part always runs"

print "\n\n"

try:
	# uncomment the below for unknown error
	b = bogus.com
	a = 0/0
except ZeroDivisionError:
	print "Divide by Zero"
except Exception as im:
	print bcolors.FAIL + str(im) + bcolors.ENDC
else:
	print bcolors.OKGREEN + "This code runs if no exception" + bcolors.ENDC
finally: 
	print "Finally, Cleanup code This part always runs"
	
