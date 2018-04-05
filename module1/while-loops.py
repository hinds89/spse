#!/usr/bin/python

# WHILE LOOPS
# See slide 40 / 67 from Module 1

age = 20
while age > 10:
	age = int(raw_input("What is your age? "))

	if age == 11 :
		print "You are 11"
		break
	if age == 12 :
		print "You Are 12"
		continue
	elif age > 10 :
		print "Your age is > 10"
	else :
		print "Your age is <= 10"
	print "end of while"
print "end of program"
