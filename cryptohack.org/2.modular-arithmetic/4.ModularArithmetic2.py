# In modular arithmetic, we often work with a modulus 'p'.
# Let's restrict ourselves to the case when 'p' is prime.

# When 'p' is prime, the integers modulo 'p' form a finite field, denoted as F_p.
# A finite field F_p consists of integers {0, 1, 2, ..., p-1}.
# In this field, both addition and multiplication have inverse elements.
# For any integer 'a' in F_p, there exists:
# - An additive inverse, 'b_add', such that a + b_add ≡ 0 mod p.
# - A multiplicative inverse, 'b_mul', such that a * b_mul ≡ 1 mod p.

# Note: The identity element for addition is 0, because a + 0 = a.
# The identity element for multiplication is 1, because a * 1 = a.

# Let's consider a prime modulus p = 17.
# First, let's calculate 3^17 mod 17 using modular arithmetic.
p = 17

# Fermat's Little Theorem states that if p is prime and a is not divisible by p,
# then a^(p-1) ≡ 1 mod p.
# For a = 3, we have:
a = 3
result_a = (a ** p) % p  # 3^17 mod 17
# By Fermat's theorem, result_a should be congruent to a mod p (result_a ≡ 3).

# Now let's calculate 5^17 mod 17.
b = 5
result_b = (b ** p) % p  # 5^17 mod 17
# Again, Fermat's theorem guarantees result_b ≡ b mod p (result_b ≡ 5).

# Try calculating 7^16 mod 17.
# Fermat's theorem suggests that a^(p-1) ≡ 1 mod p for any a not divisible by p.
# Since 7^16 mod 17 is 7^(p-1) mod 17, it should be congruent to 1 mod 17.
c = 7
result_c = (c ** (p - 1)) % p  # 7^16 mod 17

# Now consider a much larger prime modulus p = 65537.
large_p = 65537
large_number = 273246787654

# Let's calculate large_number^65536 mod 65537.
# Fermat's theorem ensures that this is congruent to 1 mod 65537.
result_large = (large_number ** (large_p - 1)) % large_p

# Outputs
print(f"3^17 mod 17 = {result_a}")
print(f"5^17 mod 17 = {result_b}")
print(f"7^16 mod 17 = {result_c}")
print(f"{large_number}^65536 mod 65537 = {result_large}")

# Fermat's Little Theorem is incredibly useful in number theory and cryptography,
# particularly for efficient modular exponentiation in RSA encryption.
# Did you manage to calculate these without a calculator? Modular arithmetic makes it simple!
