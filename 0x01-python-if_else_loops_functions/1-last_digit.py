#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

snum = str(number)
last = snum[-1]
last = int(last)

if number > 0:
    if last > 5:
        print(f"Last digit of {snum} is {last} and is greater than 5")
    elif last == 0:
        print(f"Last digit of {snum} is {last} and is 0")
    else:
        print(f"Last digit of {snum} is {last} and is less than 6 and not 0")
else:
    if last == 0:
        print(f"Last digit of {snum} is {last_digit} and is 0")
    else:
        print(f"Last digit of {snum} is -{last} and is less than 6 and not 0")
