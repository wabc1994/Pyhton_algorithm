"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
"""


def rotate_array_v1(array, k):
    if len(array) < k:
        return None
    length = len(array)
    k = k % length
    return array[length - k:] + array[:length - k]


def rotate_array_v2(array, k):
    """
    rotate the entire array "k" time
    T(n)
    :param array:  list[int]
    :param k:  int
    :return:
    """
    array = array[:]
    n = len(array)
    for i in range(k):
        # every time we save the final element in array
        temp = array[n - 1]
        for j in range(n - 1, 0 - 1):
            array[j] = array[j - 1]
        array[0] = temp
    return array


def rotate_array_v3(array, k):
    def reverse(array, a, b):
        while a < b:
            array[a], array[b] = array[b], array[a]
            a += 1
            b -= 1

    n = len(array)
    k = k % n
    reverse(array, 0, n - k - 1)
    reverse(array, n - k, n - 1)
    reverse(array, 0, n - 1)
    return array

# a= [1,2,3,4,5,6,7]
# a= [4,3,2,1,7,6,5]
# a= [5,6,7,1,2,3,4]
