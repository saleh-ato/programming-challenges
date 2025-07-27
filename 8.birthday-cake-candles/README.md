# **Birthday Cake Candles**

You are in charge of the cake for a child's birthday.
The cake will have one candle for each year of their age.
The child can only blow out the tallest candles.

Your task is to count how many candles are the tallest.

---

## **Repository Information**

* **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
* **Folder Path:** `8.birthday-cake-candles/`
* **Author:** [Saleh Ato](https://github.com/saleh-ato)

---

## **Project Overview**

This project implements a function `birthdayCakeCandles()` that receives a list of integers representing candle heights and returns the count of the tallest candles.

* The tallest candles are identified by finding the maximum height.
* The function counts how many candles have this maximum height.
* If the list is empty, the function returns 0.

---

## **Key Characteristics**

* Handles empty input gracefully.
* Efficiently finds the maximum candle height.
* Counts the occurrences of the tallest candles.
* Returns an integer representing the number of tallest candles.

---

## **Function Implementation**

```python
def birthdayCakeCandles(lst: list) -> int:
    if not lst:
        return 0
    max_val = max(lst)
    return lst.count(max_val)

# Example usage
print(birthdayCakeCandles([4,4,1,3]))  # Output: 2
print(birthdayCakeCandles([1, 1, 1, 1]))  # Output: 4
print(birthdayCakeCandles([]))  # Output: 0
```

---

## **Example Usage**

```python
print(birthdayCakeCandles([4,4,1,3]))  # 2
print(birthdayCakeCandles([1, 1, 1, 1]))  # 4
print(birthdayCakeCandles([]))  # 0
```

---

## **Notes**

* The input list can be empty or contain any positive integers.
* The function assumes candle heights are positive integers.
* Useful for problems related to counting maximum values in a list.
* Efficient for typical use cases with straightforward logic.