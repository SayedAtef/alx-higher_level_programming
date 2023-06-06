#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = abs(number) % 10
if number < 0:
    x = -x
print("Last digit of {} is {} and is ".format(number, x), end="")
if x == 0:
    print("0")
elif x > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
