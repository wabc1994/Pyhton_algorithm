from collections import deque
d = deque("12345") #构造五个元素的队列
# deque like list
d.append("6")
print(len(d))
print(d[0])
print(d)
#get the last value queue
d.pop()
#get the left value of the queue
d.popleft()
 #获取一个容量最大值为30 的队列
f = deque(maxlen=30)
# we can still extend the maxsize value
t = deque([1,2,3,4,5])
t.extend([6,7,8])
t.extendleft([0])
print(t)
