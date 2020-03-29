#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        print('*',mid, '*')
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 10, 15, 45, 98, 452]
print(binary_search(my_list, 10))
print(binary_search(my_list, 9))
