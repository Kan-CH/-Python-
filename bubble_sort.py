#coding:utf-8
def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
