#!/usr/bin/python3
def no_c(my_string):
    for i in range(str(my_string)):
        my_string = my_string.remove('c', 'C')
    print(my_string)
