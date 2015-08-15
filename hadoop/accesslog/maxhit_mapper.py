#!/usr/bin/python

# Format of each line is:
# %h %l %u %t \"%r\" %>s %b
#
import sys
url = "http://www.the-associates.co.uk"
#key = "/assets/js/the-associates.js"
for line in sys.stdin:
    data = line.strip().split(" ")
    # print "Len: ", len(data)
    rel_path = data[6]
    if rel_path.startswith(url):
        # print "ABS PATH: ", path
        rel_path = rel_path[len(url):]
        # print "REL_PATH: ",rel_path
    if rel_path == "/":
        continue
    print rel_path
