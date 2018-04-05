#!/usr/bin/env python

# This python file recursively prints a tree of directory and file structure
# from a given path downwards

def tree(path, level):
	print "----"*level,path
	for item in os.listdir(path):
		if os.path.isdir(os.path.join(path,item)):
			tree(os.path.join(path, item), level+1)
		elif os.path.isfile(os.path.join(path,item)):
			print "----" * (level+1), item
		else:
			print "unknown", item
	return

import os
path = "/home/"
print "Running tree function on path - ", path
tree(path, 0)
