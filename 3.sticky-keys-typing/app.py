'''
Sticky Keys Typing
Someone is typing on the sticky keyboard. Occasionally a key gets stuck and more than intended number
of characters of a particular letter is being added into the string. The function input contains original
and typed strings.

Determine if the typed string has been made from the original. Return true if it is and false if the typed
string cannot have been made from the original.

Examples
#function: isLongPressed(original, typed)
isLongPressed("alex", "aaleex")
output = true

isLongPressed("saeed", "ssaaedd")
#original contains 2 E's, but the typed only has 1. Not a sticky key issue.
output = false

isLongPressed("leelee", "lleeelee") 
output = true

isLongPressed("Tokyo", "TTokkyoh") 
#An h was typed, not a sticky key problem, just skill issues.
output = false

isLongPressed("laiden", "laiden") 
output = true
'''
# def normalize_with_for(text: str):
#     chars=[]
#     for i in range(len(text)):
#         if i==0 or text[i]!=text[i-1]:
#             chars+=text[i]
#     return "".join(chars)
# def normalize(text: str):
#     i=0
#     while(i<len(text)-1):
#         if text[i]==text[i+1]:
#             text=text[:i]+text[i+1:]
#             i=max(0,i-1)
#         else:
#             i+=1
#     return text
# def isLongPressed(original, typed):   # Not Correct in "leelee", "lleeelee"
#     if original==normalize_with_for(typed):
#         return True
#     else:
#         return False
# print(normalize("aaalleexxxx"))
# print(normalize_with_for("aaalleexxxx"))
# print(normalize_with_for("aaalleexxxx"))
# print(isLongPressed("alex", "aaleex")) #True

def isLongPressed(original: str, typed: str) -> bool:
    i = 0  # Pointer for original word
    j = 0  # Pointer for typed word
    
    while j < len(typed):  # Loop through each character in 'typed'
        if i < len(original) and original[i] == typed[j]:  
            # If characters match, move to the next one in both strings
            i += 1
        elif j > 0 and typed[j] == typed[j - 1]:  
            # If 'typed' character repeats the previous character, allow it
            pass
        else:
            # If neither condition is met, it's not a valid long press
            return False
        j += 1  # Move to the next character in 'typed'

    return i == len(original)  # Ensure we processed all of 'original'



print(isLongPressed("alex", "aaleex")) #True
print(isLongPressed("saeed", "ssaaedd")) #False
print(isLongPressed("leelee", "lleeelee")) #True
print(isLongPressed("Tokyo", "TTokkyoh")) #False
print(isLongPressed("laiden", "laiden")) #True