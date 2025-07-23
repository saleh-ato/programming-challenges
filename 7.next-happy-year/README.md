# **Next Happy Year**

Sloth needs your help to find the next happy year.

A **Happy Year** is a year where all digits are distinct (no duplicates).

Create a function that takes an integer year and returns the next happy year.

----------

## **Repository Information**

-   **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
    
-   **Folder Path:** `7.next-happy-year/`
    
-   **Author:** [Saleh Ato](https://github.com/saleh-ato)
    

----------

## **Project Overview**

This project implements a function `happyYear()` that receives a year as an integer and returns the next year that has all distinct digits.

-   A year is considered "happy" if none of its digits repeat.
    
-   The function finds the very next year after the input year which satisfies this condition.
    

----------

## **Key Characteristics**

-   Checks for distinct digits in the year.
    
-   Incrementally searches for the next valid year.
    
-   Uses a helper function `is_happy()` to check uniqueness of digits.
    
-   Returns a descriptive string indicating the next happy year.
    

----------

## **Function Implementation**

```python
def is_happy(year: int) -> bool:
    year_str = str(year)
    return len(set(year_str)) == len(year_str)

def happyYear(year: int) -> str:
    if is_happy(year):
        year += 1
    while not is_happy(year):
        year += 1
    return f"{year} is the next happy year with all numbers being different."

# Example usage
print(happyYear(2017))  # Output: 2018 is the next happy year with all numbers being different.
print(happyYear(1990))  # Output: 2013 is the next happy year with all numbers being different.
print(happyYear(2021))  # Output: 2031 is the next happy year with all numbers being different.
print(happyYear(2022))  # Output: 2031 is the next happy year with all numbers being different.

```

----------

## **Example Usage**

```python
print(happyYear(2017))  # 2018 is the next happy year with all numbers being different.
print(happyYear(1990))  # 2013 is the next happy year with all numbers being different.
print(happyYear(2021))  # 2031 is the next happy year with all numbers being different.
print(happyYear(2022))  # 2031 is the next happy year with all numbers being different.

```

----------

## **Notes**

-   Only integer years are accepted.
    
-   The function assumes the input year is a positive integer.
    
-   The logic can be used for any range of years.
    
-   Useful for solving date and uniqueness-related programming challenges.
    