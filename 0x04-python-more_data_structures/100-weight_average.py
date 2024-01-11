#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total = sum(value * weight for value, weight in my_list)
    weights_sum = sum(weight for _, weight in my_list)

    return total / weights_sum
