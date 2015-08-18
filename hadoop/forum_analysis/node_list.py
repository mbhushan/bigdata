#!/usr/bin/python


import sys
import csv
import re


patt = re.compile(r'\W+')
reader = csv.reader(sys.stdin, delimiter="\t")
firstrow = True
key = "fantastically"

for line in sys.stdin:
    row = line.strip()
    # row = re.findall(r"[\"](.*?)[\"]", row)
    # print row
    # print "TYPE: ", type(row)
    if firstrow:
        firstrow = False
        continue
    # if len(row) < 5:
    #    continue
    words = patt.split(row)
    print "WORDS: ", words
    for w in words:
        cand = w.lower()
        if cand == key:
            print cand



