#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return None  # Return None instead of 'None' string
    else:
        return my_list[idx]
