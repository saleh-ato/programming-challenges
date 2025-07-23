"""
Next Happy Year
Sloth needs your help to find out the next happy year.

A Happy Year is the year with only distinct digits (no duplicates).

Create a function that takes an integer year and returns the next happy year.

Examples
happyYear(2017)
output = 2018
# 2018 is the next happy year with all numbers being different.

happyYear(1990)
output = 2013
# 2013 is the next happy year with all numbers being different.

happyYear(2021)
output = 2031
# 2031 is the next happy year with all numbers being different.
"""
def is_happy(year:int)->bool:
    year_str=str(year)
    return len(set(year_str)) == len(year_str)
def happyYear(year:int)->str:
    if is_happy(year):
        year+=1
    while(not is_happy(year)):
        year+=1
    return f"{year} is the next happy year with all numbers being different."

print(happyYear(2017))
print(happyYear(1990))
print(happyYear(2021))
print(happyYear(2022))