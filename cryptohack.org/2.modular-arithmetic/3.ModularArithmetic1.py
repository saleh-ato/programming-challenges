# Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin:
# 4 + 9 = 1
# 5 - 7 = 10
# 2 + 3 = 5
# At first glance, this might seem nonsensical—perhaps a sign of madness!
# However, these equations are valid in modular arithmetic modulo 12 (though with some sloppy notation).
# Modular arithmetic is often something you've been doing without realizing, like when you calculate time.
# For example, 9 hours after 5 o'clock is 2 o'clock: (9 + 5) % 12 = 2.

# Mathematically, we describe modular arithmetic with congruences.
# Two integers are congruent modulo m if a ≡ b mod m.
# This means when integer a is divided by m, the remainder is b.
# For example:
#  11 ≡ 5 mod 6 (since 11 divided by 6 leaves a remainder of 5)
# 8146798528947 ≡ 4 mod 17 (huge numbers work too—modular arithmetic simplifies them!)

# Let's compute the following integers:
# 1. Solve 11 ≡ x mod 6
x = 11 % 6  # Result: x = 5

# 2. Solve 8146798528947 ≡ y mod 17
y = 8146798528947 % 17  # Result: y = 4

# The solution is the smaller of these two integers: (x, y).
solution = min(x, y)

# Outputs
print(f"11 ≡ {x} mod 6")
print(f"8146798528947 ≡ {y} mod 17")
print(f"The smaller result is {solution}")
