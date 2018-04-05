#!/usr/bin/env python

# the following code taken from https://www.programiz.com/python-programming/user-defined-exception
# accessed 6/2/2018

# define Python user defined exceptions
class Error(Exception):
	"""Base class for other exceptions"""
	pass

class ValueTooSmallError(Error):
	"""Raised when the input value is too small"""
	pass

class ValueTooLargeError(Error):
	"""Raised when the input value is too large"""
	pass

# main program
# user guesses a number until they get it right

# you need to guess this number
number = 8

while True:
	try:
		i_num = int(input("Enter a number: "))
		if i_num < number:
			raise ValueTooSmallError
		elif i_num > number:
			raise ValueTooLargeError
		break
	except ValueTooSmallError:
		print("This is too small, try again!\n")
	except ValueTooLargeError:
		print("This value is too large, try again!\n")
	except Exception as im:
		print im

print("Congratulations! You guessed it correctly.")
