#coding:utf-8
def quick_sort(list):
    left = []
    right = []
    pivotList = []
    if len(list) <= 1:
        return list
    pivot = list[0]
    for i in list:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            pivotList.append(i)
    left = quick_sort(left)
    right = quick_sort(right)
    return left + pivotList + right
