import csv
import re


def csv_reader(num_lines):

    patt = re.compile(r'\W+')
    with open("../data/forum_node.tsv", "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            print patt.split(row[4])
            num_lines -= 1
            if num_lines < 1:
                break


def main():
    num_lines = 5
    csv_reader(num_lines)

if __name__ == '__main__':
    main()
