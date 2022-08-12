#!/usr/bin/python3
''' Integer addition in test driven development'''


def add_integer(a, b=98):
    ''' A function that adds 2 integers a and b

    a and b must be first casted to integers if they are float

    a and b must be integers or floats

    Raises:
        TypeError: a must be an integer or b must be an integer
    '''
    if a != type(int) and  a != type(float):
        raise TypeError('a must be an integer')
    if b != type(int) and b != type(float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
