"""
Design a data structure that supports all following operations
in average O(1) time.
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
Each element must have the same probability of being returned.
how to decide a key whether in a python dictionary
if val in 字典即可
remove the element from the num , let the require remove to be the first element
字典
"""
import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.index = {}

    def insert(self, val):
        if val not in self.index:
            self.nums.append(val)
            self.index[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        return true if remove successfully, use the replace 填补法即可
        拿最后一个元素填补上去即可
        :param val: the value need to replace
        :return:
        """
        if val in self.index:
            idx, last = self.index[val], self.nums[-1]
            self.nums[idx], self.index[last] = last, idx
            self.nums.pop()
            self.index.pop(val, 0)
            return True
        return False

    def get_random(self):
        index = random.randint(0, len(self.nums) - 1)
        return self.nums[index]


if __name__ == '__main__':
    rs = RandomizedSet()
    print("insert 1: ", rs.insert(1))
    print("insert 2: ", rs.insert(2))
    print("insert 3: ", rs.insert(3))
    print("insert 4: ", rs.insert("4"))
    print("remove 3: ", rs.remove(3))
    print("get_random: ", rs.get_random())
    print(len(rs.nums))
