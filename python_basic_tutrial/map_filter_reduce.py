"""
map(function, item), function define by user or lambda ,item include list
we can pass more than one iterable item
we can get a map object
"""
def calculateSquare(n):
    return n*n

numbers = [1, 2, 3, 4, 5]
result = list(map(calculateSquare, numbers))

print(result)
numbers_square = set(result)
print(numbers_square)

# the true thing behind map
def map(func, iterable):
    for i in iterable:
        yield func(i)

#example add two more function
def multiply(x):
    return (x*x)
def add(x):
    return (x*2)
func1 = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), func1))
    print(value)

# or just as the same
def map_2(func, iterable):
    result = []
    for i in  iterable:
        #do something for i func(i)
        result.append(func(i))
    return result

#range give us  filter(func, iterable item)
number_list = list(range(-5, 5))
less_than_zero = list(filter(lambda x: x<0, number_list))
print(number_list)

# reduce
#without reduce
product = 1
list_1 = list(range(0,5))
for num in list_1:
    product = product * num
import operator
# using the reduce ,实现联成操作
from functools import reduce

result = list(reduce(operator.add, list_1))
print(result)

