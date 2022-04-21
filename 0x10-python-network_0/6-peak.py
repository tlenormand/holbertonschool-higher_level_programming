#!/usr/bin/python3
""" 6 """


def find_peak(list_of_integers):
    """find the biggest number of the list"""
    if list_of_integers == []:
        return None

    li = list_of_integers

    if int(len(list_of_integers) / 2) - 1 < 0 and \
       int(len(list_of_integers) / 2) + 1 >= len(list_of_integers):
        return li[int(len(list_of_integers) / 2)]
    elif int(len(list_of_integers) / 2) - 1 < 0:
        return li[int(len(list_of_integers) / 2)]\
               if li[int(len(list_of_integers) / 2)] >\
               li[int(len(list_of_integers) / 2) + 1]\
               else li[int(len(list_of_integers) / 2) + 1]
    elif int(len(list_of_integers) / 2) + 1 >= len(list_of_integers):
        return li[int(len(list_of_integers) / 2)] if \
               li[int(len(list_of_integers) / 2)] > \
               li[int(len(list_of_integers) / 2) - 1] \
               else li[int(len(list_of_integers) / 2) - 1]

    if li[int(len(list_of_integers) / 2) - 1] < \
       li[int(len(list_of_integers) / 2)] > \
       li[int(len(list_of_integers) / 2) + 1]:
        return li[int(len(list_of_integers) / 2)]

    if li[int(len(list_of_integers) / 2) + 1] \
       > li[int(len(list_of_integers) / 2) - 1]:
        return find_peak(li[int(len(list_of_integers) / 2):])
    return find_peak(li[:int(len(list_of_integers) / 2)])
