#!/usr/bin/env python

# define class using class keyword
class Calculator:

	# Constructor of class
	# This runs when you instantiate an object of this class
	def __init__(self, ina, inb):
		self.a = ina
		self.b = inb

	def add(self):
		return self.a + self.b

	def mul(self):
		return self.a*self.b

# A new class that inherits from the Calculator class
class Scientific(Calculator):
	def power(self):
		return self.a**self.b

def quickAdd(a,b):
	return a+b
