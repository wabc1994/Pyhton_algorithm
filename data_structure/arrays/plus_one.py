"""
一个整数使用数组存储，最高位在左边，最低位在右边
Given a non-negative number represented as an array of digits,
plus one to the number.
The digits are stored such that the most significant
digit is at the head of the list.
"""


def plus_one(nums_1):
    """

    :param nums: list[int]
    :return: list[int]
    """
    nums_1[-1] = nums_1[-1] + 1
    res = []
    ten = 0
    i = len(nums_1) - 1
    while i >= 0 or ten == 1:
        sum = 0
        if i >= 0:
            sum += nums_1[i]
        if ten:
            sum +=1
        res.append(sum % 10)
        ten = sum //10
        i -= 1
    return res[::-1]

"""
第二种方法是采用判断，如果最后一位小于9 
则直接相加返回值即可
"""

def plus_one_v2(nums):
    n = len(nums)
    "类似于for(int i=n;i<n;i++) 从后面向前面循环处理"
    for i in range(n-1,-1,-1):
        if(nums[i]) <9:
            nums[i] +=1
            return nums
        nums[i] = 0
    nums.insert(0,1)
    return nums




"第三种办法"
def plus_one_v3(nums_2):
    for idex, digit in reversed(enumerate(nums_2)):
        nums_2[idex] = (nums_2[idex]+1) % 10
        "如果第一次都没有通过该结果"
        if nums_2[idex]:
            return nums_2
        "如果没有多余的值可以直接返回"
        return [1] + nums_2