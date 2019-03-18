def bubble_sort(array):
    """
    Given an array of data, sort the array.  The bubble sort, or sinking sort, steps through the list and swaps
    items, repeating as necessary until the list is sorted.  It's not a practical sort algorithm to use as there
    are other algorithms with better worst case performance.

    Reference: https://en.wikipedia.org/wiki/Bubble_sort

    Example:
    ```python
        unsorted = [2, 1, 5, 4, 3]
        sorted = bubble_sort(unsorted)
        # sorted is = [1, 2, 3, 4, 5]
    ```
    """
    sorted = False
    sorted_array = array
    while sorted is False:
        sorted = True
        for i in range(len(sorted_array) - 1):
            if sorted_array[i] > sorted_array[i + 1]:
                swap(sorted_array, i, i + 1)
                sorted = False
    return sorted_array


def swap(array, x, y):
    """
    Given an array, and two valid index locations, swap the items at the locations with one another.  If invalid
    indices are given, python will raise an exception.

    Example:
    ```python
        array = [1, 2, 3, 4, 5]
        swap(array, 0, 1)
        # array now = [2, 1, 3, 4, 5]
    ```
    """
    array[x], array[y] = array[y], array[x]
