----------

# **Shuffled Properly**

Determine whether a list of integers from 1 to 10 is shuffled well enough—meaning it avoids ordered streaks of 3 or more consecutive numbers (either ascending or descending).

----------

## **Repository Information**

-   **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
-   **Folder Path:** `5.shuffled-properly/`
-   **Author:** [Saleh Ato](https://github.com/saleh-ato)

----------

## **Project Overview**

This challenge provides a Python function `isShuffledWell()` that analyzes a list of 10 integers and checks whether it exhibits good randomness. If three or more numbers appear consecutively—either increasing like `[1,2,3]` or decreasing like `[9,8,7]`—the array is considered **not** well shuffled.

📌 Only differences of exactly ±1 are considered consecutive.

----------

## **Key Characteristics**

-   **Checks for Ordered Sequences:** Identifies ascending or descending runs of 3 consecutive numbers.
-   **Strict Rule for Shuffling:** Even a single trio in order invalidates the shuffle.
-   **Linear Scan Logic:** No sorting is used, preserving original order during validation.

----------

## **Function Implementation**

```python
from typing import List

def isShuffledWell(array: List[int]) -> bool:
    for i in range(2, len(array)):
        sub_array = [array[i-2], array[i-1], array[i]]
        if (
            sub_array[2] == sub_array[1] + 1 and sub_array[1] == sub_array[0] + 1
        ) or (
            sub_array[0] == sub_array[1] + 1 and sub_array[1] == sub_array[2] + 1
        ):
            return False
    return True

```

----------

## **Example Usage**

```python
array1 = [1, 2, 3, 5, 8, 6, 9, 10, 7, 4]
print(isShuffledWell(array1))  # False → 1,2,3 are consecutive

array2 = [3, 5, 1, 9, 8, 7, 6, 4, 2, 10]
print(isShuffledWell(array2))  # False → 9,8,7,6 are descending

array3 = [1, 5, 3, 8, 10, 2, 7, 6, 4, 9]
print(isShuffledWell(array3))  # True → no streaks found

array4 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(isShuffledWell(array4))  # True → no ordered sequences

array5 = [4, 6, 5, 8, 7, 9, 10]
print(isShuffledWell(array5))  # False → 7,8,9 and 8,9,10

```

----------

## **Notes**

-   Only strict steps of 1 in either direction count as consecutive.
-   The function assumes the input is a list of integers ranging from 1 to 10.
-   Useful for validating randomness in card shuffling, list scrambling, or number distribution tasks.

----------