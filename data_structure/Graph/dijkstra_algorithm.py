import math
import sys

class PriorityQueue:
    def __init__(self):
        """
        based on minHeap
        array contains all the element
        """
        self.cur_size = 0
        self.array = []
        self.pos = {}

    def isEmpty(self):
        return self.cur_size == 0

    def min_heapify(self, idx):
        """

        :param idx: 开始调整的下标位置，调整最小堆，
        然后再对其左右孩子结点进行调节
        :return:
        """
        lc = self.left(idx)
        rc = self.right(idx)
        if lc < self.cur_size and self.array[lc][0] < self.array[idx][0]:
            smallest  = lc
        else:
            smallest = idx
        if rc < self.cur_size and self.array[rc][0] < self.array[smallest][0]:
            smallest = rc
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def insert(self, tup):
        #insert a node into a priority Queue
        self.pos[tup[1]] = self.cur_size
        self.cur_size += 1
        self.array.append((sys.maxsize, tup[1]))
        self.decrease_key((sys.maxsize, tup[1],tup[0]))

    def extract_min(self):
        min_node = self.array[0][1]
        self.array[0] = self.array[self.cur_size-1]
        self.cur_size -= 1
        self.min_heapify(1)
        del self.pos[min_node]
        return min_node

    def right(self,i):

        return 2 * i + 2

    def left(self, i):
        return 2 * i + 1

    def par(self, i):
        return math.floor( i/2)

    def swap(self, i, j):
        self.pos[self.array[i][1]] =  j
        self.pos[self.array[j][1]] = i
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp



