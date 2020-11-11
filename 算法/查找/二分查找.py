# -*- coding:utf-8 -*-
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:       
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == "__main__":
    my_list = [0,1,2,3,4,5,6,7,8,9]
    for item in my_list:
        val = binary_search(my_list,item)
        print(item, val)


