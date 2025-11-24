def sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) < 2:
        return arr[0]
    pivot = arr[0]
    return pivot + sum(arr[1:])
