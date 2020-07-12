

def selection_sort(arr):
    i = 0
    n = len(arr)

    while i < n:
        min_pos = i
        j = i+1
        while j < n:
            if arr[j] <= arr[min_pos]:
                min_pos = j
            j += 1
        
        if min_pos != i:
            tmp = arr[i]
            arr[i] = arr[min_pos]
            arr[min_pos] = tmp
        i += 1
    return arr

l = [39, 37, -2, 0, 5, 3, -29]

print(selection_sort(l))
