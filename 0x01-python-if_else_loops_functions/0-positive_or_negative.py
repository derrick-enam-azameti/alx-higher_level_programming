#!/usr/bin/python3
import random
num = random.randint(-10, 10)
if num < 0:
    print("{:d} is negative".format(num))
elif num > 0:
    print("{:d} is positive".format(num))
else:
    print("0 is zero")
