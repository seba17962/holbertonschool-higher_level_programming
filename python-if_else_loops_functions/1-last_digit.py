#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)
last_digit = last_digit[-1]
if (int(last_digit) > 5 and number > 0):
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif (int(last_digit) < 6 and number > 0):
    print(f"Last digit of {number} is {last_digit} \
        and is less than 6 and not 0")
elif (number < 0):
    print(f"Last digit of {number} is -{last_digit} \
        and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
