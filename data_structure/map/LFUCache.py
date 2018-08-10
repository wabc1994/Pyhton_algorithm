from collections import OrderedDict
from collections import defaultdict

class LFUCache(object):

    MIN = -1
    def __init__(self, capacity):
        """

        :param capacity: 缓存容量初始化
        """
        self.cap = capacity
        self.val = {}
        self.count = {}
        self.lists = defaultdict(OrderedDict)

    def get(self,key):
        """

        :param key:访问一次
        :return: if val contain key ,then return the value, or return -1
        """
        if key not in self.val:
            return -1

        count = self.count[key]
        self.count[key]= count+1
        self.lists[count].pop(key)

        if(count==LFUCache.MIN) and self.lists[count]==0:
            LFUCache.MIN+=1
        self.lists[count+1][key] =None
        return self.val[key]

    def set(self,key, value):
        if key in self.val:
            self.val[key]= value
            self.get(key)

        if len(self.val)==self.cap:
            evict= next(self.lists[LFUCache.MIN].keys())
            self.lists[LFUCache.MIN].pop(evict)
            self.val.pop(evict)
            self.count.pop(evict)

        self.val[key] = value
        self.count[key] = 1
        LFUCache.MIN = 1
        self.lists[1][key]=None