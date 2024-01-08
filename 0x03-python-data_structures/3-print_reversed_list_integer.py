#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None or not my_list:  # Handle None and empty list cases
        return
    
    reversed_list = reversed(my_list)
    for num in reversed_list:
        print("{:d}".format(num))
