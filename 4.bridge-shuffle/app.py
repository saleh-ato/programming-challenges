'''
Bridge Shuffle
Create a function to bridge shuffle two arrays.

To bridge shuffle, you interleave the elements from both arrays in an alternating fashion:

array1 = ["A", "A", "A"]
array2 = ["B", "B", "B"]

shuffled_array = ["A", "B", "A", "B", "A", "B"]
This can still work with two arrays of uneven length. We simply tack on the extra elements from the longer array:

array1 = ["C", "C", "C", "C"]
array2 = ["D"]

shuffled_array = ["C", "D", "C", "C", "C"]
Examples
bridgeShuffle
'''
def BridgeShuffle(arr1, arr2):
    result=[]
    longer_arr=arr1
    if len(arr1)<len(arr2):
        longer_arr=arr2
    for i in range(len(longer_arr)):
        try:
            # print(i)
            # print(arr1[i])
            result.append(arr1[i])
            result.append(arr2[i])
        except Exception as e:
            # print(e)
            pass
    return result

array1 = ["A", "A", "A"]
array2 = ["B", "B", "B"]
print(BridgeShuffle(array1,array2)) #["A", "B", "A", "B", "A", "B"]

array1 = ["C", "C", "C", "C"]
array2 = ["D"]
print(BridgeShuffle(array1,array2)) #["C", "D", "C", "C", "C"]
