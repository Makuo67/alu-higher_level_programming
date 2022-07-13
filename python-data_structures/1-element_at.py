#!/usr/bin/python3
def element_at(my_list, idx):
    for i in idx:
        if i == -i:
            return None
        elif i > len(my_list):
            return None
        else:
            print()
