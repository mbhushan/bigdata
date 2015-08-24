#!/usr/bin/python


import sys
import csv
import re


patt = re.compile(r'\W+')
# reader = csv.reader(sys.stdin, delimiter="\t")
firstrow = True
key = "fantastically"
count = 0
limit = 10
last = None
curr = None
with open("forum_users.tsv", "rb") as f:
    print "inside with.."
    for line in f:
        keys = patt.split(line)
        keys = filter(None, keys)
        # print "Keys: ", keys
        if keys[0] and keys[0].isdigit():
            print keys[0]
exit()

for line in sys.stdin:
    row = line.strip()
    # row = re.findall(r"[\"](.*?)[\"]", row)
    # print row
    # print "TYPE: ", type(row)
    if firstrow:
        firstrow = False
        continue
    # if count == limit:
    #    break
    words = patt.split(row)
    if words[0].isdigit():
        curr = words[0]

    # print "WORDS: ", words
    for w in words:
        cand = w.lower()
        if cand == key:
            print cand, " ", curr
    # count += 1



