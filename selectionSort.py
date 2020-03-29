#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import random

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


arr = list(np.random.randint(10, 100, 10))
print('原数组:    ', arr)
print('选择排序后:', selectionsort(arr))