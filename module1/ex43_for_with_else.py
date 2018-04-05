#!/usr/bin/python

# This is demonstrating the else clause of the for loop in python
# A good reference website, accessed 20/07/2016:
# 	 https://shahriar.svbtle.com/pythons-else-clause-in-loops


x = range(1, 10, 2)

# Demonstrates the continue statement - immediately jumps to the next iteration of the for loop and skips any statements after it.
for item in x:
	if item is 5:
		print "item is 5"
		continue
	print item
else:
	print "The loop finished ok :)!"

print '\n'*2

# The following code demonstrates the break and else not running.
for item in x:
	if item is 5:
		print "item is 5"
		break
	print item
else:
	print "Else" # This code won't run since the loop was terminated by a break
	
