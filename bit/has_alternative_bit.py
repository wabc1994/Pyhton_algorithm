"""
Given a positive integer, check whether it has alternating bits:namely,
if two adjacent bits will always have different，连续的两位均不相同
前提条件是正整数，可以不考虑负号位数
"""

def  has_alternative_bit(n):
    """
    #time complexity -  O(numeber of bits in n)
    :param n:
    :return:
    """
    first_bit = 0
    second_bit = 0
    while n:
        first_bit = n & 1
        if n >>1:
            second_bit = (n>>1) & 1
            if not first_bit ^ second_bit:
                return False
        else:
            return False
        n = n >> 1
        #经过所有的田间
    return True
"""
class solution{
public boolean class_solution(int n)
{
    string s = Integer.toBinaryString(n);
    for(int i=0;i<s.length()-1;i++)
    {
        if(s.charAt(i)== s.charAt(i+1))
            return false
            
    }
    return true
}
}
"""

def has_alternative_fast(n):
    mask1 = int('aaaaaaaa', 16)  # for bits ending with zero (...1010)
    mask2 = int('55555555', 16)  # for bits ending with one  (...0101)
    return mask1 == (n + (n ^ mask1)) or mask2 == (n + (n ^ mask2))