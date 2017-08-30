#coding:utf-8
def shell_sort(list):
    count = len(list)
    step = 2
    d = count/step
    while d > 0:
        for i in range(0, d):
            j = i + d
            while j < count:
                k = j - d
                key = list[j]
                while k >=0:
                    if list[k] > key:
                        list[k+d] = list[k]
                        list[k] = key
                    k -= d
                j += d
        d /= step
    return list
