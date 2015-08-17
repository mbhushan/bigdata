import hashlib


def gen_user_buckets():
    bucket80 = 0
    bucket20 = 0
    with open("email_ids.csv", "rb") as f:
        for line in f:
            st = line.split("@")[0]
            st = line
            m = hashlib.md5(st)
            md5 = m.hexdigest()
            res = md5[-6:]
            value = int(res, 16)
            mod = value % 100
            if mod < 80:
                bucket80 += 1
            else:
                bucket20 += 1
    print "Bucket 80 count: ", bucket80
    print "Bucket 20 count: ", bucket20


def main():
    gen_user_buckets()


if __name__ == '__main__':
    main()
