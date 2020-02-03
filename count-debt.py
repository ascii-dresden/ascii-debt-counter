#!/usr/bin/python3

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


def read_input(amounts: list):
    """Reads the input for the amount of bills and coins in the register."""

    for coin in staggering:
        try:
            amounts[coin] = int(input('Amount of {:1.2f}€: '.format(coin)))
        except ValueError:
            pass
        print('  {:1.2f}€ × {:2d} = {:5.2f}€'.format(coin, amounts[coin],
                                                     coin * amounts[coin]))


read_input(amounts)

# Calculate coin amount value
for coin in staggering:
    total += amounts[coin] * coin

total = round(total, 2)

headings = [*map(lambda x: "{:1.2f}€".format(x), reversed(staggering)), " Summe "]
values = [
    *map(lambda x: "{:5d}".format(x), reversed(amounts.values())),
    "{:5.2f}€ ".format(total)
]

print("\nValues for table:")

print("┌─{}─┐".format("─┬─".join(map(lambda x: "─" * len(x), values))))

print("│ {} |".format(" │ ".join(headings)))

print("├─{}─┤".format("─┼─".join(map(lambda x: "─" * len(x), values))))

print("│ {} |".format(" │ ".join(values)))

print("└─{}─┘".format("─┴─".join(map(lambda x: "─" * len(x), values))))

print("Check these again, to be sure you didn't make a typo.\n")

print("Sum: {:1.2f}€".format(total))
