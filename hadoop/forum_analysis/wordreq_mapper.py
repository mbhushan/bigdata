#!/usr/bin/python


import sys
import csv


patt = re.compile(r'\W+')
reader = csv.reader(sys.stdin, delimiter="\t")
firstrow = True
key = "fantastic"

for row in reader:
    if firstrow:
        firstrow = False
        continue
    words = patt.split(row[4])
    for w in words:
        if w.lower() == key:
            print w.lower()



