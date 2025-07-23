


# **Next in the Alphabet**

Create a function that returns the next alphabetical string based on the given input. The function increments the last letter alphabetically, carrying over like counting in base-26 when reaching 'Z'.

----------

## **Repository Information**

-   **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
    
-   **Folder Path:** `6.next-in-the-alphabet/`
    
-   **Author:** [Saleh Ato](https://github.com/saleh-ato)
    

----------

## **Project Overview**

This project implements the function `next_letters()` which takes an uppercase alphabetical string and returns the "next" string in alphabetical order.

-   The function treats letters like digits in a base-26 number system where 'A' corresponds to 0 and 'Z' to 25.
    
-   When the last character is 'Z', it rolls over to 'A' and carries over to the previous character, similar to numeric addition.
    
-   Empty input returns "A".
    

----------

## **Key Characteristics**

-   Supports carrying over multiple letters (e.g., "Z" → "AA", "CAZ" → "CBA").
    
-   Input is case-insensitive but output is always uppercase.
    
-   Mimics incrementing a number but with letters.
    
-   Treats empty string as 0 and returns 'A'.
    

----------

## **Function Implementation**

```python
def next_letter(char: str = None) -> tuple[str, int]:
    carry = 0
    if char is None or len(char) != 1:
        print("Input must be a single character.")
    next_char = chr(ord(char.upper()) + 1)
    if next_char == "[":
        carry = 1
        next_char = "A"
    return (next_char, carry)

def next_letters(string: str = None) -> str:
    if string == "" or string is None:
        return "A"
    string = string.upper()
    index = len(string) - 1
    last_char, carry = next_letter(string[index])
    string = string[:index] + last_char
    while carry == 1:
        index -= 1
        if index < 0:
            string = "A" + string
            carry = 0
        else:
            carry_char, carry = next_letter(string[index])
            string = string[:index] + carry_char + string[index + 1 :]
    return string

```

----------

## **Example Usage**

```python
print(next_letters("A"))      # Output: B
print(next_letters("ABC"))    # Output: ABD
print(next_letters("Z"))      # Output: AA
print(next_letters("CAZ"))    # Output: CBA
print(next_letters(""))       # Output: A
print(next_letters("zzz"))    # Output: AAAA
print(next_letters("Zzzz"))   # Output: AAAAA

```

----------

## **Notes**

-   The function only accepts letters A-Z (case-insensitive).
    
-   Empty input is treated as 0 and returns 'A'.
    
-   The logic simulates base-26 addition with carry over.
    
-   Useful for problems requiring alphabetical incrementing similar to spreadsheet column naming.
    

----------
