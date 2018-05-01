#!/usr/bin/env python

import signal


# write a signal handler
def ctrlc_handler(signum, frm) :
	print "Haha! CTRL+C won't work to kill this program"

print "Installing signal handler ..."
signal.signal(signal.SIGINT, ctrlc_handler)
print "Done!"

# Infinite loop
while True:
	pass
