#!/usr/bin/python

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    # writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"',
    #                    quoting=csv.QUOTE_ALL)

    for line in reader:
        buf = list()
        if len(line) >= 10:
            for i in range(10):
                if i == 4:
                    continue
                buf.append(line[i])
            buf.insert(0, "N")
            buf.insert(0, line[3])
        if len(line) <= 5:
            for i in range(1, 5):
                buf.append(line[i])
            buf.insert(0, "U")
            buf.insert(0, line[0])
        data = '\t'.join('"%s"' % (s) for s in buf)
        print data
        # writer.writerow(data)


def main():
    mapper()


if __name__ == '__main__':
    main()
