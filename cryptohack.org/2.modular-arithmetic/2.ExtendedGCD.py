'''
Let a and b be positive integers.
The extended Euclidean algorithm is an efficient way to find integers u,v such that
a.u+b.v=gcd(a,b)
Later, when we learn to decrypt RSA ciphertexts, we will need this algorithm to calculate the modular inverse of the public exponent.
Using the two primes p=26513,q=32321, find the integers u,v such that
p.u+q.v=gcd(p,q)
Enter whichever of u and v is the lower number as the flag.
Knowing that p,q are prime, what would you expect gcd(p,q) to be? For more details on the extended Euclidean algorithm, check out this page.
'''
p=26513
q=32321

# 𝑝(𝑎)+𝑠(𝑏)=GCD(𝑎,𝑏)
def extended_gcd(a, b):
    # خط 1: بررسی شرط پایه
    if b == 0:
        return a, 1, 0  # GCD، ضرایب p و s بازگردانده می‌شوند.
    
    # خط 2: فراخوانی بازگشتی
    gcd, p1, s1 = extended_gcd(b, a % b)
    
    # خط 3: به‌روزرسانی ضرایب
    p = s1
    s = p1 - (a // b) * s1
    
    # خط 4: بازگشت نتیجه
    return gcd, p, s

# خط 5: استفاده از تابع برای مثال مشخص
a = 81
b = 57
gcd, p, s = extended_gcd(a, b)

# خط 6: چاپ نتیجه
print(f"GCD({a}, {b}) = {gcd}")
print(f"Coefficients: p = {p}, s = {s}")


p=26513
q=32321
print(extended_gcd(p,q))