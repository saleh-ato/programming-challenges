'''
No Yelling
Create a function that transforms sentences ending with multiple question marks ?
or exclamation marks ! into a sentence only ending with one without changing punctuation
in the middle of the sentences.

Examples
noYelling("What went wrong?????????")
output = "What went wrong?"

noYelling("Oh my goodness!!!")
output = "Oh my goodness!"

noYelling("I just!!! can!!! not!!! believe!!! it!!!")
output = "I just!!! can!!! not!!! believe!!! it!"
# Only change repeating punctuation at the end of the sentence.

noYelling("Oh my goodness!")
output = "Oh my goodness!"
# Do not change sentences where there exists only one or zero exclamation marks/question marks.
Notes
Only change ending punctuation - keep the exclamation marks or question marks in the middle of the sentence the same (see third example).

Don't worry about mixed punctuation (no cases that end in something like ?!??!).

Keep sentences that do not have question/exclamation marks the same.
'''
def noYelling(s: str) -> str:
    if not s:
        return s
    last_char = s[-1]
    if last_char not in ['!', '?']:
        return s
    # Counting
    count = 1
    for i in range(len(s)-2, -1, -1):
        if s[i] == last_char:
            count += 1
        else:
            break
    # Removing Duplicate signs at the end of the string
    if count > 1:
        s = s[:-count] + last_char

    return s

# Test
print(noYelling("What went wrong?????????"))  # "What went wrong?"
print(noYelling("Oh my goodness!!!"))        # "Oh my goodness!"
print(noYelling("I just!!! can!!! not!!! believe!!! it!!!"))  # "I just!!! can!!! not!!! believe!!! it!"
print(noYelling("I just!!! can!!! not!!! believe!!! it!!!!!!!"))  # "I just!!! can!!! not!!! believe!!! it!"
print(noYelling("Oh my goodness!"))          # "Oh my goodness!"