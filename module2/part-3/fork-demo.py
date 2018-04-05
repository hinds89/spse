#!/usr/bin/env python

import os

def child_process():
	print "I am the child process and my PID is: %d"%os.getpid()
	print "The child is exiting"

def parent_process():
	print "I am the parent process and my PID is: %d"%os.getpid()
	
	childpid = os.fork()

	if childpid == 0:
		# we are inside the child
		print "I am the CHILD - Go do child_process."
		child_process()
	else:
		# we are inside the parent process
		print "We are inside the PARENT process"
		print "Our child has PID: %d"%childpid

	while True:
		pass

parent_process()
