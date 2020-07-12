
def sort(my_list):
    #merge_sort_top_down(my_list)
    merge_bottom_up(my_list)


def merge_bottom_up(my_list):
    """
    A bottom up merge sort that uses a fixed size stack space.
    Time complexity is O(n lg n) and uses n-length auxilary array for merges.

    """
    n = len(my_list)

    aux = [None] * n

    length = 1
    while length < n:
        lo = 0
        while lo < n - length:
            merge_bu_helper(my_list, aux, lo, lo+length-1, min(lo+length+length-1, n-1))
            lo += length + length
        length *= 2


def merge_bu_helper(my_list, aux, lo, mid, hi):
    if hi <= lo: return
    i = lo
    j = mid + 1

    k = lo
    while k <= hi:
        aux[k] = my_list[k]
        k += 1    

    k = lo
    while k <= hi:
        if i > mid:
            my_list[k] = aux[j]
            j += 1
        elif j > hi:
            my_list[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            my_list[k] = aux[j]
            j += 1
        else:
            my_list[k] = aux[i] 
            i += 1
        k += 1


def merge_sort_top_down(my_list):
    """
    Runs in O(n lg n) time and requires space proprotional to input list for the auxillary arrays.  
    
    """
    if len(my_list) > 1:
        mid = len(my_list)//2
        left = my_list[:mid]
        right = my_list[mid:]

        merge_sort_top_down(left)
        merge_sort_top_down(right)
        
        merge(left, right, my_list)


def merge(left, right, my_list):

    """
    Abstract in-place merge that takes two input lists, 'left' and 'right' and merges them in 'my_list'.
          
    """

    assert(is_sorted(left))
    assert(is_sorted(right))

    i, j, k  = 0, 0, 0
    print(len(aux), len(my_list))
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            my_list[k] = left[i]
            i += 1
        else:
            my_list[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        my_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        my_list[k] = right[j]
        j += 1
        k += 1


"""
Helper methods.
"""

def is_sorted(my_list):
    for i in range(len(my_list)-1):
        if my_list[i+1] < my_list[i]: 
            return False
    return True



if __name__ == '__main__':
    l = [-3, -4, -5, -6, 0, 100, -33]
    sort(l)
    print(l)

