#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    value = 0
    for nums in my_list:
        total += (nums[0] * nums[1])
        value += nums[1]
    return (total / value)
