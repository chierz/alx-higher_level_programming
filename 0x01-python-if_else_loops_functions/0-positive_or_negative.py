#!/usr/bin/python3

import random
number = -256 #random.randint(-10000, 10000) # -256 # the_last_digit = -6
if number < -9:
    the_last_digit = number % -10
elif number > 9:
   the_ last_digit = number % 10
if the_last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif the_last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero")
elif the_last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
