#!/usr/bin/env python

import random

ina = int(raw_input('Please enter number of possible outcomes: '))
inb = int(raw_input('Please enter number of samples for each survey (integer): '))
inc = int(raw_input('Please enter total number of surveys (integer): '))

for i in range(0,inc):
	# generate a random number between 1 and ina
	# do this inb times for each survey
	count = 0
	for item in range(0, inb):
		randnum = random.randint(1,ina)
		count = count + randnum
		# print 'randnum = ', randnum, 'count = ', count
	else:
		average = float(count)/float(inb)
		print 'i = ', i, 'average = ', average
