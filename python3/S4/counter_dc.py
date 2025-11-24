def counter(arr):
    if len(arr) < 2 :
        return len(arr)
    return 1 + counter(arr[1:])
