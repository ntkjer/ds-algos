import math

def qsort(my_list):
    quick_sort(my_list, 0, len(my_list)-1)

def quick_sort(my_list, lo, hi):
    if lo < hi:
        k = partition_a(my_list, lo, hi)
        quick_sort(my_list, lo, k - 1)
        quick_sort(my_list, k + 1, hi)


def partition(my_list, lo, hi):
    pivot = my_list[hi + lo // 2]
    i = lo
    j = hi + 1
    while True:
        while my_list(i) < pivot:
            if i == hi:
                break
#        while pivot < my_list[j]

def partition_a(my_list, lo, hi):
    i = lo-1
    pivot = my_list[hi]
    for j in range(lo, hi):
        if my_list[j] <= pivot:
            i = i + 1
            my_list[i], my_list[j] = my_list[j], my_list[i],

    my_list[i+1], my_list[hi] = my_list[hi], my_list[i+1]
    return i + 1

def lomuto_partition(my_list, lo, hi):
    pivot = my_list[hi]
    j = i = lo
    while j < hi:
        if my_list[j] < pivot:
            swap = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = swap
            i += 1

    swap = my_list[i]
    my_list[i] = my_list[hi]
    my_list[hi] = swap
    return i



    return

if __name__ == '__main__':
    l = [-3, -4, -5, -6, 0, 10, -199]
    print(qsort(l))
