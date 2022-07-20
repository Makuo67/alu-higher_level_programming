#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    funct = 0
    for i in range(x):
        try:
            my_list.append(i)
            if i == type(str):
                my_list.remove(i)
            funct += 1
        except (ValueError, TypeError):
            break
    print("{:d}".format(my_list[0]), end="")

