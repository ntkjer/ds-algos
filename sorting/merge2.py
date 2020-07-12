
def sort(arr):
    #merge_sort_top_down(arr, 0, len(arr)-1)
    merge_sort_bottom_up(arr)

def merge_sort_bottom_up(arr):
    n = len(arr)

    length = 1
    while length < n:
        lo = 0
        while lo < n-length:
            merge(arr, lo, lo+length-1, min(lo+length+length-1, n-1))
            lo += length + i
        length *= 2


def merge_sort_top_down(arr, lo, hi):
    """
    Recursive mergesort that sorts item in O(n lg n) time. 
    Maintans a stack size of lg n items propotional to input. 

    """

    if hi <= lo: return

    mid = lo + (hi-lo) / 2
    # Sort left and right half recursively.
    merge_sort_top_down(arr, lo, mid)
    merge_sort_top_down(arr, mid+1, hi)

    #Merge 
    merge(arr, lo, mid, hi)

def is_sorted(arr):
    return is_sorted(arr, 0, len(arr-1))


def is_sorted(arr, lo, hi):
    i = 0
    while i <= hi:
        if arr[i] < arr[i-1]:
            return False
        i += 1

def merge(arr, lo, mid, hi):
    aux = []

    k = lo 

    # Copy to auxilary array
    while k <= hi:
        aux[k] = arr[k]
        k += 1
    
    i, j = lo, mid+1    

    # Mergback to input arr
    while k <= hi:    
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1
        k += 1


#l = [-2, -4, -5, -1, 0, -13, 100, -123, 5]
l = [-2, -4, -6]  

sort(l)

print(l)
