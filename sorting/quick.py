import math

def qsort(my_list):
    n = len(my_list) - 1
    return quick_sort(my_list, 0, n), quick_sort_3(my_list, 0, n)

def quick_sort(my_list, lo, hi):
    if lo >= hi: return
    k = partition(my_list, lo, hi)
    quick_sort(my_list, lo, k - 1)
    quick_sort(my_list, k + 1, hi)
    return my_list

def partition(my_list, lo, hi):
    i = lo-1
    pivot = my_list[hi]
    for j in range(lo, hi):
        if my_list[j] <= pivot:
            i = i + 1
            my_list[i], my_list[j] = my_list[j], my_list[i]

    my_list[i+1], my_list[hi] = my_list[hi], my_list[i+1]
    return i + 1

def quick_sort_3(my_list, lo, hi):
    if hi <= lo: return
    lt, i, gt = lo, lo+1, hi
    v = my_list[lo]
    while i <= gt:
        comparison = compare(my_list[i], v)
        if comparison < 0: 
            swap(my_list, lt, i)
            i += 1
        elif comparison > 0:
            swap(my_list, i, gt)
            gt -= 1
        else:
            i += 1

    quick_sort_3(my_list, lo, lt -1)
    quick_sort_3(my_list, gt + 1, hi)
    return my_list


def swap(my_list, j, k):
    my_list[j], my_list[k] = my_list[k], my_list[j]

def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

if __name__ == '__main__':
    l = [-3, -4, -5, -6, 0, 10, -199]
    a, b = qsort(l)
    print("quick sort: ", a)
    print("quick sort, 3 way part: ", b)
