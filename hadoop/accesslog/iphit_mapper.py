#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    ipaddr = data[0]
    print ipaddr 
