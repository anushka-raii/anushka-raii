#Write a function raise_to_power(base, exponent) that returns the value of base raised to the exponent power.
def raise_to_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base

print(raise_to_power(2, 3)) 
