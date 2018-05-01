#!/usr/bin/env python
# see the readme.txt file for attribution of where I got this code
# note I've changed it a bit from the original.
# I've added the change to path of script from this website https://stackoverflow.com/questions/1432924/python-change-the-scripts-working-directory-to-the-scripts-own-directory 
# accessed 6 April 2018

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

print "abspath"
print abspath
print "dname"
print dname

with open("Fortune500.txt","r") as f, open('f500.txt', 'w') as out:
    for line in f:
        new_str = ''.join(line.split('www')[1:])
            #concatenate ftp to striped address
        sftp = "ftp"
        ftp2be = sftp + new_str
        #print ftp2be


        out.write(ftp2be)
