# -*- coding:utf-8 -*-
def quick_sort(arr):
    "快速排序，选择基准值，将比之小的放左边，比之大的放右边，时间复杂度：O(n*logn)"
    if len(arr) < 2:
        return arr
    else:
        base = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i <= base:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [base] + quick_sort(right)

# 优雅的写法
def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    pivot = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= pivot]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

array = [4,2,1,5,7,8,3,4,3,2,1]
print(quick_sort(array))