#!/usr/bin/python3
''' Integer addition in test driven development'''


def add_integer(a, b=98):
     """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if a != type(int) and  a != type(float):
        raise TypeError('a must be an integer')
    if b != type(int) and b != type(float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
