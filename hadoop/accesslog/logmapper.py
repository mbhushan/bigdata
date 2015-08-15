#!/usr/bin/python

# Format of each line is:
# %h %l %u %t \"%r\" %>s %b
#
import sys
#key = "/assets/js/the-associates.js"
for line in sys.stdin:
    data = line.strip().split(" ")
    print "Len: ", len(data)
    print data
    # if any(key in s for s in data):
    #    result = "yes"
    # index = line.strip().find("/assets/js/the-associates.js")
