#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("{:02d}".format(i), end=", ")
        continue
    if i == 99:
        print("{:02d}".format(i))
        break
    print("{:02d}".format(i), end=", ")
