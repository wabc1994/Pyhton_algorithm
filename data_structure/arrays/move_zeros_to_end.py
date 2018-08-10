"""
write an algorithm that takes an array and moves all
all of the zeros to the end
 preserving  the order of the other elements
        move_zeors([false, 1,0,1,2,0,1,3,'a'] )
        return => ([false, 1,1,2,1,3,'a',0,0])
the time complexity of the below algorithms is 0(n)
"""

def move_zeors(array):
    result =[]
    zeros =0
    for i in array:
        if i is 0:
            zeros +=1
        else:
            result.append(i)
            " not append are extend"
    result.extend([0] * zeros)
    return result