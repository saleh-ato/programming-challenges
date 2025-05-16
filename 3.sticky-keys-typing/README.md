# **Sticky Keys Typing**

Write a function that verifies if a typed string is a valid long-pressed version of an original string. Occasionally, keys on a keyboard get stuck, leading to unintended repeated characters. The function isLongPressed() determines whether the typed string could have been produced from the original by long-pressing keys.

## **Repository Information**
- **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
- **Folder Path:** `3.sticky-keys-typing/`
- **Author:** [Saleh Ato](https://github.com/saleh-ato)

---

## **Project Overview**
This repository provides a Python function, `isLongPressed()`, which checks whether a given typed string is a valid representation of an original string with occasional long-pressed characters.


**Key Characteristics:**
- **Handles Sticky Keys:** Repeated characters are allowed if they match the previous one in the typed string.
- **Strict Character Order:** Characters in `typed` must follow the sequence of `original` without extra letters.
- **Optimized Processing:** Uses two-pointer technique for efficient verification.

---

## **Example Usage**
Below are some examples demonstrating how the function works:

```python
print(isLongPressed("alex", "aaleex"))  # Output: True
print(isLongPressed("saeed", "ssaaedd"))  # Output: False
print(isLongPressed("leelee", "lleeelee"))  # Output: True
print(isLongPressed("Tokyo", "TTokkyoh"))  # Output: False
print(isLongPressed("laiden", "laiden"))  # Output: True
```

---

## **Function Implementation**
```python
def isLongPressed(original: str, typed: str) -> bool:
    i = 0  # Pointer for original string
    j = 0  # Pointer for typed string

    while j < len(typed):  # Iterate through typed characters
        if i < len(original) and original[i] == typed[j]:  
            # If characters match, move both pointers
            i += 1
        elif j > 0 and typed[j] == typed[j - 1]:  
            # Allow repeated characters if they match the previous typed letter
            pass
        else:
            # If neither condition is met, return False
            return False
        j += 1  # Move typed pointer forward

    return i == len(original)  # Ensure original was fully processed
```