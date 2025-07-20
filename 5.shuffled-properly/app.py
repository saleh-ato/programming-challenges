'''
Shuffled Properly?
Given an array of 10 numbers, return whether or not the array is shuffled enough.

In this case, if 3 or more numbers appear consecutively (ascending or descending), return false.

Examples
isShuffledWell([1, 2, 3, 5, 8, 6, 9, 10, 7, 4])
output = false
# 1, 2, 3 appear consecutively

isShuffledWell([3, 5, 1, 9, 8, 7, 6, 4, 2, 10])
output = false
# 9, 8, 7, 6 appear consecutively

isShuffledWell([1, 5, 3, 8, 10, 2, 7, 6, 4, 9])
output = true
# No consecutive numbers appear

isShuffledWell([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
output = true
# No consecutive numbers appear
Notes
Only steps of 1 in either direction count as consecutive (i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).

You will get numbers from 1-10.
'''
from typing import List

def isShuffledWell(array:List[int])->bool:
    flag=False
    sub_array=[]
    for i in range(2,len(array)):
        # print(array[i])
        # sub_array=sorted([array[i-2],array[i-1],array[i]])
        sub_array=[array[i-2],array[i-1],array[i]]
        # print(sub_array)
        if (sub_array[2]==sub_array[1]+1 and sub_array[1]==sub_array[0]+1) or (sub_array[0]==sub_array[1]+1 and sub_array[1]==sub_array[2]+1):
            return False
    return True
array1=[1, 2, 3, 5, 8, 6, 9, 10, 7, 4]
array2=[3, 5, 1, 9, 8, 7, 6, 4, 2, 10]
array3=[1, 5, 3, 8, 10, 2, 7, 6, 4, 9]
array4=[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
array5 = [4, 6, 5, 8, 7, 9, 10]


# isShuffledWell(array1)
print(isShuffledWell(array1))
print(isShuffledWell(array2))
print(isShuffledWell(array3))
print(isShuffledWell(array4))
print(isShuffledWell(array5))
