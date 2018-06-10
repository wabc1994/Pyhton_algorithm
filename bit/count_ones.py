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

def count_1(n):
    count = 0
    while n:
        if( n & 1):
            count +=1
            n >> 1
    return count


"""
OFFER中提供的解法，逐个判断最右边的数是否为1，然后右移动一位，判断接下的为一位
比如0101，先判断右起第一位是不是1，(和1做与运算，如果是1，则结果是1，如果是0，则结果0)然后再右移动一位变成0010，接着判断"
"""


"""时间复杂度为0（log(n)），空间复杂度为O(1)"""

