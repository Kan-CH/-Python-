#coding:utf-8
def insert_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0:
            if list[j] > key:
                list[j+1] = list[j]
                list[j] = key
            j -= 1
    return list
