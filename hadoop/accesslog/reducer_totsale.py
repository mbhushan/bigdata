#!/usr/bin/python

import sys

salesTotal = 0
numSales = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales from the store will be added
# All the sales from the store would be counted in numSales var

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    salesTotal += float(thisSale)
    numSales += 1

print salesTotal, "\t", numSales 

