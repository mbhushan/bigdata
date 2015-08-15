#!/usr/bin/python

import sys

ipcount = 0
total_count = 0
prev_ip = None

for line in sys.stdin:
    curr_ip = line.strip()

    if prev_ip and prev_ip != curr_ip:
        print prev_ip, "\t", total_count
        total_count = 0
        prev_ip = curr_ip

    prev_ip = curr_ip
    total_count += 1
 
if prev_ip != None:
    print prev_ip, "\t", total_count
    
