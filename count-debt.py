#!/usr/bin/python3

import datetime
# Script for counting money for ascii Dresden.
# This is fairly well written python. One of my first little projects.

name = "MyName"

# Array that contains the values of rows.
staggering = [1.5, 1, .8, .5, .2, .1]

# Arrays for amounts of the bills and coins.
amounts = {coin: 0 for coin in staggering}

"""
Integers for money amount.

```total``` is the sum of all the money in the register.
"""
total = 0


def read_input(amounts : list):
    """Reads the input for the amount of bills and coins in the register."""

    for coin in staggering:
        try:
            amounts[coin] = int(input('Amount {}: '.format('{:1.2f}'.format(coin))))
        except ValueError:
            print("NaN")


read_input(amounts)

print("\nValues for table:")
print(*amounts.values(), sep=', ')
print("Check these again, to be sure you didn't make a typo.\n")

# Calculate coin amount value
for coin in staggering:
    total += amounts[coin] * coin

total = round(total, 2)

print("Sum: " + str(total))
