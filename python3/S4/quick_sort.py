def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = []
    pivot.append(arr[0])
    less = []
    greater = []
    for x in arr[1:] :
        if x < pivot[0] :
            less.append(x)
        else:
            greater.append(x)
    return quick_sort(less) + pivot + quick_sort(greater)
