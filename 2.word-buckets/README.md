# **Word Buckets**

Write a function that divides a phrase into word buckets, where each bucket contains _n_ or fewer characters. The buckets include only complete words—no word is split between buckets.

## **Repository Information**
- **Main Repository:** [Programming Challenges](https://github.com/saleh-ato/programming-challenges)
- **Folder Path:** `2.word-buckets/`
- **Author:** [Saleh Ato](https://github.com/saleh-ato)

---

## **Project Overview**
This repository provides a Python function, `split_into_buckets()`, that takes a phrase and a maximum character limit per bucket, and then returns a list of buckets. Each bucket is a string containing full words whose total length (including spaces) does not exceed the given character limit.

**Key Characteristics:**
- **Complete Words Only:** Words are never broken across buckets.
- **Optimized Grouping:** Buckets are created in a way that they pack as many words as possible without exceeding the maximum character limit.
- **Input Sanitization:** Leading and trailing spaces are removed before processing.

---

## **Example Usage**
Below are some examples demonstrating how the function works:

```python
split_into_buckets("she sells sea shells by the sea", 10)
# Output: ["she sells", "sea shells", "by the sea"]

split_into_buckets("the mouse jumped over the cheese", 7)
# Output: ["the", "mouse", "jumped", "over", "the", "cheese"]

split_into_buckets("fairy dust coated the air", 20)
# Output: ["fairy dust coated", "the air"]

split_into_buckets("a b c d e", 2)
# Output: ["a", "b", "c", "d", "e"]
