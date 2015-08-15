#!/usr/bin/python

# Format of each line is:
# %h %l %u %t \"%r\" %>s %b
#
import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 7:
        ip, iden, uname, time, req, status, objsize = data
	print data
        #print "{0}\t{1}".format(store, cost)

