#!/usr/bin/env python

import sys

def print5times(line_to_print):
	for count in range(0,5):
		print line_to_print

print5times(sys.argv[1])
i = 0
for item in sys.argv:
	print "argv[" + str(i) + "] = " + item
	i+=1
