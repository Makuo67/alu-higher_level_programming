#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        my_string = my_string.remove('c', 'C')
    print(my_string)
