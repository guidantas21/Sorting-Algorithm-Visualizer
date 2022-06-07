def insertionSortAlgorithm(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key


def insertionSort(array, ascending=True):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        if ascending:

            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j -= 1

            array[j+1] = key

        else:

            while j >= 0 and key > array[j]:
                array[j+1] = array[j]
                j -= 1

            array[j+1] = key

def create_list(n, min_value, max_value):
    from random import randint
    return [randint(min_value, max_value) for _ in range(n)]


# == INPUT ==
n = 10
min_value = 0
max_value = 50
ascending = False

array = create_list(n, min_value, max_value)
not_sorted_array = array[:]


# == ALGORITHM ==
insertionSort(array, ascending)


# == OUTPUT ==
print(f"({'ascending' if ascending else 'descending'}) {not_sorted_array} --> {array}")
