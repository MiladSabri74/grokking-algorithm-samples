ASCENDING = True
DESCENDING = False

def find_smallest(values):
    min_value = values[0]
    min_index = 0
    for i in range(1, len(values)) :
        if values[i] < min_value:
            min_value = values[i]
            min_index = i
    return min_index

def find_biggest(values):
    max_value = values[0]
    max_index = 0
    for i in  range(1, len(values)) :
        if values[i] > max_value:
            max_value = values[i]
            max_index = i
    return max_index

def selection_sort(vals, direction):
    values = vals.copy()
    result = []
    for _ in range(len(values)):
        j = 0
        if direction == ASCENDING:
            j = find_smallest(values)
        else :
            j = find_biggest(values)
        result.append( values.pop(j))
    return result


vals = [3,6,5,4,1]
print(selection_sort(vals,True))
print(selection_sort(vals,False))