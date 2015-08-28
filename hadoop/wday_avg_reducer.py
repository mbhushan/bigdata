#!/usr/bin/python

import sys


wday_dict = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # something went wrong - lets ignore and continue
        continue
    wkey = data[0]
    saleval = float(data[1])
    count = 1
    if wkey in wday_dict:
        wdata = wday_dict[wkey]
        count= count + wdata[0]
        saleval = saleval + wdata[1]
    wday_dict[wkey] = (count, saleval)
for key, val in wday_dict.items():
    avg_sale = float(val[1]/val[0])
    print "{0}\t{1}".format(key, avg_sale)
