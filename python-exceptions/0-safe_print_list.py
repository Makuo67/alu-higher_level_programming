#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    while True:
        try:
            my_list.append(x)
            return my_list
        except ValueError:
            print()
print(safe_print_list(my_list=[], x=7))

