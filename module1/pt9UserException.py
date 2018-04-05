#!/usr/bin/env python

# lots of info for the below code is from: https://www.programiz.com/python-programming/user-defined-exception
# accessed 6/02/2018
class UserException(Exception):
	"""There was an ambiguous error"""
	pass

print "class UserException has been defined, derived from the Exception class"
#print "\n\nRaising UserException Error"
#raise UserException

print "\n\nRaise UserException with custom error message"
raise UserException("Here's my custom error message")
