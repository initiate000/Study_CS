# -*- coding:utf-8 -*-
def binary_search(list, item):
    '二分查找，在有序列表中查询一个数'
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

def binary_search_recrusive(list,low,high,item):
    '用递归的方式来进行二分查找'
    if low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            return binary_search_recrusive(list,low,mid-1,item)
        else:
            return binary_search_recrusive(list,mid+1,high,item)
    else:
        return None


if __name__ == "__main__":
    my_list = [0,1,2,3,4,5,6,7,8,9]
    for item in my_list:
        val_1 = binary_search(my_list,item)
        val_2 = binary_search_recrusive(my_list,0,len(my_list)-1,item)
        print(item, val_1,val_2)
