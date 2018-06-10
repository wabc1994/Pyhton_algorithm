"""
the following code add two positive integers without using
the "+" operator
the code uses bitwise operation to add two numbers
input :2 3
output: 5

"""
def add_bitwise_operator(x, y):
    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

a = add_bitwise_operator(4, 5)
print(a) 