'''
Factorial of Factorials
Create a function that takes an integer n and returns the factorial of factorials.
See below examples for a better understanding:

Examples
fact_of_fact(4)
output = 288
// 4! * 3! * 2! * 1! = 288

fact_of_fact(5)
output = 34560

fact_of_fact(6)
output = 24883200
'''
def Fact(n: int) -> int:
    fact=1
    for i in range(n, 1, -1):
        fact*=i
    return fact

def fact_of_fact(n: int) -> int:
    result=1
    for i in range(n,1,-1):
        result*=Fact(i)
    return result

print(fact_of_fact(4)) #288
print(fact_of_fact(5)) #34560
print(fact_of_fact(6)) #24883200
# __________OR(Better Performance)__________

from math import factorial, prod

def fact_of_fact2(n: int) -> int:
    result=1
    for i in range(n,1,-1):
        prod(result,factorial(i))
    return result

print(fact_of_fact(4)) #288
print(fact_of_fact(5)) #34560
print(fact_of_fact(6)) #24883200