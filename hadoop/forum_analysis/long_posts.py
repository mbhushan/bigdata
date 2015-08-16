#!/usr/bin/python
"""
Your mapper function should print out 10
lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""

import sys
import csv
from Queue import PriorityQueue


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)
    pq = PriorityQueue()
    topsize = 10
    result = []

    for line in reader:
        # YOUR CODE HERE
        post = line[4]
        if pq.qsize() < topsize:
            pq.put(post)
        else:
            minpost = pq.get()
            if len(minpost) >= len(post):
                pq.put(minpost)
            else:
                pq.put(post)
    for i in range(topsize):
        result.append(pq.get())
        # writer.writerow(line)
    result.sort(key=len)
    for r in result:
        print r


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""


# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__

main()
