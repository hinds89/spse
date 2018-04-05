#!/usr/bin/python

import sys

def print5times(line_to_print):
	
	for count in range(0,5):
		print str(count) + " " + line_to_print

print5times(sys.argv[1])
