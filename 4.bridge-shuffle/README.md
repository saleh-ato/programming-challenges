# **Bridge Shuffle**

Write a function that interleaves two lists in an alternating fashion, ensuring that elements from both lists are shuffled together. If one list is longer than the other, remaining elements from the longer list are appended at the end.
## **Repository Information**
- **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
- **Folder Path:** `4.bridge-shuffle/`
- **Author:** [Saleh Ato](https://github.com/saleh-ato)

---

## **Project Overview**
This repository provides a Python function, `BridgeShuffle()`, which takes two lists and combines them in an alternating pattern. If the lists have different lengths, the extra elements from the longer list are added to the end.


**Key Characteristics:**
- **Alternating Shuffle:** Each element from both lists is placed in turn.
- **Handles Uneven Lists:** The function correctly accounts for cases where lists have different lengths.
- **Optimized for Simplicity:** Uses a loop with exception handling to avoid index errors.

---

## **Example Usage**
Below are some examples demonstrating how the function works:

```python
array1 = ["A", "A", "A"]
array2 = ["B", "B", "B"]
print(BridgeShuffle(array1, array2))  
# Output: ["A", "B", "A", "B", "A", "B"]

array1 = ["C", "C", "C", "C"]
array2 = ["D"]
print(BridgeShuffle(array1, array2))  
# Output: ["C", "D", "C", "C", "C"]
```
---

## **Function Implementation**
```python
def BridgeShuffle(arr1, arr2):
    result = []
    longer_arr = arr1 if len(arr1) >= len(arr2) else arr2

    for i in range(len(longer_arr)):
        try:
            result.append(arr1[i])
            result.append(arr2[i])
        except IndexError:
            pass  # Handles cases where one list is shorter

    return result
```
