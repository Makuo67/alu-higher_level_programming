#!/usr/bin/python3
def print_last_digit(number):
    for c in number:
        print(f'{number[-1:]:d}', end="")
