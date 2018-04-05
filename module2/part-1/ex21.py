#! /usr/bin/env python

with open('/var/log/syslog', 'r') as f:
	for line in f:
		if line.lower().find('usb') >= 0:
			print line,

print 'File Closed: ' + str(f.closed)
