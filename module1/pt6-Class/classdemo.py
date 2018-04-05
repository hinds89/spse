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

# define an object of type Calculator
ina = float(raw_input('Enter first number: '))
inb = float(raw_input('Enter second number: '))

newCalculation = Calculator(ina,inb)

print 'a+b = %d' %newCalculation.add()

print 'a*b = %d' %newCalculation.mul()

newPower = Scientific(ina, inb)

print '\n\na pow b: %d' %newPower.power()

print 'a+b = %d' %newPower.add()

print 'a*b = %d' %newPower.mul()

atest = Scientific
print newCalculation.a
