"""
位数从右边开始算起，0，1，2，3，4，5，6，7 一共八位
Fundamental bit operation:
      get_bit(num, i) :get an exact bit at specific index
      set_bit(num, i): set a bit at specific index
      clear_bit(num, u): clear a bit at specific index
      update_bit(num,i ,bit): update a bit at specific index
"""
def get_bit(num, i):
    """
    this function shifts 1 over by i bits, creating a value
    being  like 0001000,by performing an and with num ,we clear all
    bits  other than the bit at bit i finally we compare that to 0
    :param num:
    :param i:
    :return:
    """
    return (num & (1<<i)) != 0

def set_bit(num, i):
    """
    this function shift 1 over by i bits， creating a value being like 00001000
    by performing an or with num ,only value at bit i will change

    :param num:
    :param i:
    :return:
    """
    return num | (1<<i)

def clear_bit(num, i):
    """
    把第二i位设置为0，无论原来的位数是多少
    :param num:
    :param i:
    :return:
    """
    mask = ~(1<<i)
    return num & mask


def updata_bit(num, i, bit):
    """
    th
    :param num:
    :param i:
    :param bit:
    :return:
    """
    mask = ~(1<<i)
    return (num & mask) | (bit<<i)