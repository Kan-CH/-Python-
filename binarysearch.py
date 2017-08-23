#coding:utf-8
def binarysearch(list,key):
    list.sort()
    lo = 0
    hi = len(list)-1
    while lo <= hi:
        mid = lo + (hi - lo)/2
        if key < list[mid]:
            hi = mid
        elif key > list[mid]:
            lo = mid
        else:
            return mid
    return -1
