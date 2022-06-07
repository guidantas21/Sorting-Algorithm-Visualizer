def bubbleSortAlgorithm(array):
    n = len(array)
    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def bubbleSort_optimized(array):
    n = len(array)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break


def bubbleSort(array, ascending=True):
    n = len(array)
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):

            if (ascending and array[j] > array[j+1]) or (not ascending and array[j] < array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break


def create_list(n, min_value, max_value):
    from random import randint
    return [randint(min_value, max_value) for _ in range(n)]


# == INPUT ==
n = 10
min_value = 0
max_value = 50
ascending = True

array = create_list(n, min_value, max_value)
not_sorted_array = array[:]

# == ALGORITHM ==
bubbleSort(array, ascending)

# == OUTPUT ==
print(f"({'ascending' if ascending else 'descending'}) {not_sorted_array} --> {array}")
