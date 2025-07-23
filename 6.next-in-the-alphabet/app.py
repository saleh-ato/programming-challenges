'''
Next in the Alphabet
Create a function which returns the next letters alphabetically in a given string. If the last letter is a "Z", change the rest of the letters accordingly.

Examples
next_letters("A")
output = "B"
// 'A' becomes 'B' – simple increment.

next_letters("ABC")
output = "ABD"
// 'C' becomes 'D' – last character changes without carry.

next_letters("Z")
output = "AA"
// 'Z' rolls over to 'A', and since there's no previous letter, we add a new 'A'.
// Think of it like 9 + 1 = 10, here Z + 1 = AA.

next_letters("CAZ")
output = "CBA"
// 'Z' → 'A' (carry), 'A' → 'B' (no carry), so "CAZ" becomes "CBA".
// Like incrementing 129 → 130 but in letters.

next_letters("")
output = "A"
// Empty input is treated as 0 → return 'A'.
Notes
Tests will all be in CAPITALS.

Empty inputs should return a capital "A" (as if it were in letter position 0!).

Think about the letter "Z" like the number 9 and how it carries over to increment the next letter/digit over.
'''
def next_letter(char:str=None)->tuple[str,int]:
    carry=0
    if char is None or len(char) != 1:
        print("Input must be a single character.")
    next_char=chr(ord(char.upper())+1)
    if next_char=="[":
        carry=1
        next_char="A"
    return (next_char,carry)

def next_letters(string:str=None)->str:
    if string=="" or string==None:
        return "A"
    string=string.upper()
    index=len(string)-1
    last_char=string[-1]
    last_char,carry=next_letter(last_char)
    # print(last_char,carry)
    if carry==0:
        string=string[:index]+next_letter(string[index])[0]
    elif carry==1:
        string=string[:index]+next_letter(string[index])[0]
        while carry==1:
            # CAZ->CBA
            carry_char,carry=next_letter(string[index-1])
            string=string[:index-1]+carry_char+string[index:]
            index-=1
            if index ==0:
                string="A"+string
                break
    else:
        return None
    return string

# __________First tests__________
# print(next_letters()) #Expected: A | Result: A
# print(next_letters("")) #Expected: A | Result: A
# __________Second tests__________
# print(next_letters("a")) #Expected: B | Result: B
# print(next_letters("abcd")) #Expected: ABCE | Result: ABCE
# __________Third tests__________
# print(next_letters("CAZ")) #Expected: CBA | Result: CBA
# print(next_letters("CAZZ")) #Expected: CBAA | Result: CBAA
# print(next_letters("vwxyz")) #Expected: VWXZA | Result: VWXZA
# __________Last tests__________
print(next_letters("zzz"))  #Expected: AAAA | Result: AAAA
print(next_letters("Zzzz")) #Expected: AAAAA | Result: AAAAA
