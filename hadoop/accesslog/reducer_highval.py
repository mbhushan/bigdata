#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
maxVal = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    # maxVal = 0

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", maxVal
        oldKey = thisKey;
        # salesTotal = 0
        maxVal = 0

    oldKey = thisKey
    if float(thisSale) > float(maxVal):
        maxVal = thisSale
    # salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", maxVal

