"""
将多维数组转换为一维数组
Iterable

Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.

"""
from collections import Iterable


# return a list
# None ploy  the role of contain value ,so we do not need to additionl set a value for return
# every time we need to analysis or

def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for element in input_arr:
        if isinstance(element, Iterable):
            flatten(element, output_arr)
        else:
            output_arr.append(element)
    return output_arr


# return iterator

def flatten_iter(iterable):
    """
    :param iterable: an input multi dimensional iterable and return generator which
    produces one dimensional output
    :return:
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten(element)

        else:
            yield element


def main():
    # d
    result = flatten([[1, 2], [2, 3]])
    print(result)
    result_iterable = flatten_iter([1, 2, 3, [1, 4, 5]])
    print(result_iterable)


if __name__ == "__main__":
    main()
