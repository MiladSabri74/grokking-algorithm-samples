def binary_search(values, wanted):
    min_index = 0
    max_index = len(values)-1
    while min_index <= max_index :
        searched_index = (min_index + max_index) // 2
        if values[searched_index] == wanted :
            return searched_index
        elif wanted > values[searched_index] :
            min_index = searched_index + 1
        else :
            max_index = searched_index - 1
    return -1

