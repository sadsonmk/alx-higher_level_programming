#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    len1 = len(my_list_1)
    len2 = len(my_list_2)
    new_list = []
    y = 0
    try:
        if len1 != len2:
            print("out of range")
        while y < list_length:
            if type(my_list_1[y]) == str or type(my_list_2[y]) == str:
                print("wrong type")
                new_list.append(0)
            if my_list_2[y] == 0:
                print("division by 0")
                new_list.append(0)
            else:
                new_list.append(my_list_1[y] / my_list_2[y])
            y = y + 1
    except:
        pass
    finally:
        return new_list
