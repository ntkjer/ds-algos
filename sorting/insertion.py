def insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    i = 1
    while i < len(arr):
        curr = arr[i] 
        j = i-1

        while j >= 0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = curr
        i += 1

    return arr

if __name__ == '__main__':
    l = [100, 20, 0, -20, -30]
    print(insertion_sort(l))
