#!/usr/bin/python

# Part 3, Exercise - While loops with "else" (see slide 41)
# 
# Reference, accessed 19/7/16 - 
# http://www.tutorialspoint.com/python/python_while_loop.htm

age = 0

while age < 10:
	print "Your age, " + str(age) + ", is < 10"
	age = int(raw_input("What is your age ? "))
else :
	print "Your age is not less than 10."
