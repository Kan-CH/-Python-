#coding:utf-8
def select_sort(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if (list[i] < list[j]):
                t = list[i]
                list[i] = list[j]
                list[j] = t
    return list
