"""
implementation io priority queue using linear array
Insert -O(n)
Extract min/max Node -O(1)
the big one in the deque head,
"""
import collections

class PriorityQueueNode:
    def __init__(self, data, priority):
        """

        represent the item of priority_queue
        :param data: the data part
        :param priority: the priority of the data
        """
        self.data = data
        self.priority = priority

    def __repr__(self):
        return str(self.data) + ":" + str(self.priority)


class PriorityQueue(object):
    def __init__(self):
        self.priority_queue_list = collections.deque

    def __repr__(self):
        return "PriorityQueue({!r})".format(list(self.priority_queue_list))

    @property
    def size(self):
        return len(list(self.priority_queue_list))

    def push(self, item, priority=None):
        """

        :param item:  the node
        :param priority:
        :return:
        """
        priority = item if priority is None else priority
        node = PriorityQueueNode(item, priority)
        for index, current in enumerate(self.priority_queue_list):
            if current.priority > node.priority:
                self.priority_queue_list.insert(index,current)
                return

        self.priority_queue_list.append(node)

    def pop(self):
        return  self.priority_queue_list.popleft()
