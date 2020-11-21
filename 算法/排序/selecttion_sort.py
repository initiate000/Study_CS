# -*- coding:utf-8 -*-
def find_smallest(arr):
    "find the smallest number in arr"
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    "选择排序，每次选择最小的数，O（n^2）"
    newarr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr

print(selection_sort([5,3,2,7,10,0]))
