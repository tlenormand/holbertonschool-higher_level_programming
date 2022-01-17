#!/usr/bin/python3
"""function that divides element by element 2 lists

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of the list

    Return:
        new list (length = list_length) with all divisions
"""


def list_division(my_list_1, my_list_2, list_length):

    idx = 0
    new_list = [0] * list_length

    while list_length > 0:

        try:
            new_list[idx] = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            new_list[idx] = 0
        except IndexError:
            print("out of range")
            new_list[idx] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[idx] = 0
        finally:
            list_length -= 1
            idx += 1

    return new_list
