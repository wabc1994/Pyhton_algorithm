# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    #一样的思路


    # 断开成两部分，一部分开始的没有含有结点，PRE指向头结点，
    # 刚开始的时候为空的结点,
    # reverse 和 reverse 的区别是

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
      #get the linkedlist into two part

  #pre 指向REVERSE    第一个结点，而 head 还是指向原先结点的第一个结点，最后在指向第一个结点即可
    # 先把聊边断开成两部分，第一部分剩余一个第一个结点，其余的采用插入法连接起来，
    def reverse_1(self):
        pre = self.head
        current = self.head
        r = current.next
        current.next = None
        current = r
        while(current):
            r = current.next
            current.next = pre
            pre = current
            current = r
        self.head = pre


    # Function to insert a new node at the beginning ,采用不带头结点的单链表 ，并且采用
    # 头插法
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node



    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Driver program to test above functions
if __name__ == '__main__':

    llist = LinkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    print("given a list")
    llist.printList()
    llist.reverse_1()
   # llist.reverse()
    llist.printList()