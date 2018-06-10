"""
write a function that takes an unsigned integer
return the number of "1" bit it has
(also know as the hamming weight)
for example, the 32-bit integer "11" has binary
representation 0000 0000 0000 0000 0000 0000 0000 1011
return three
不断消除最后有一位
"""

def count_ones_recur(n):
    """
    using brain kernighan 's algorithm. (recursive approach)

    :param n:
    :return:
    """
    if not n:
        return 0
    return 1 + count_ones_recur(n & (n-1))



def count_ones_iter(n):
    """using brain keranighan algorithm (iterative approach)
    """
    count = 0
    while n:
        count += 1
        n &=(n-1)
    return count

"""时间复杂度为0（log(n)），空间复杂度为O(1)"""

