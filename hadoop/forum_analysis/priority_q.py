from Queue import PriorityQueue


nums = [4, 2, 9, 12, 32, 1, 5, 25, 13, 19, 3, 10]
top = 3


def main():
    print "Input list of numbers are: "
    print nums
    pq = PriorityQueue()
    for n in nums:
        if pq.qsize() < top:
            pq.put(n)
        else:
            minval = pq.get()
            key = max(n, minval)
            pq.put(key)
    print "Top {0} values are:".format(top)
    for i in range(top):
        print pq.get()


if __name__ == "__main__":
    main()
