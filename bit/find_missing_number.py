"""
return the missing number from a sequence of unique
integers in range[0:n] in O(n) time and space. The dif
"""

def find_missing_number(nums):
    """
    :param nums: the number array
    :return: the missing number
    """
    missing  = 0
    n = len(nums)
    for i, element  in enumerate(nums):
        missing ^= element
        missing ^= (i+1)
    missing ^= (n+1)
    return missing


def find_missing_number2(nums):
    nums_sum = sum(nums)
    n = len(nums)
    total_sum = (n+1)*n // 2
    misssing =  total_sum-nums_sum
    return misssing

if __name__ == '__main__':
    nums =[1,5,3,4]
    print(find_missing_number(nums))
    print(find_missing_number2(nums))