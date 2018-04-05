#!/usr/bin/python

import sys

# This function is to count the number of command line arguments
# this is from the following website, accessed 26/07/2016:
#  http://www.tutorialspoint.com/python/python_command_line_arguments.htm
def cmdargs():
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)
	# print 'argc = ', str(argc)

# This function is to say hello to name
def sayHello(name):
	print "Hello there :", name

# run the below to show how the above functions run
cmdargs()
name = raw_input('What is your name: ')
sayHello(name)
