# Custom Power Calculator
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print("2^3 =", power(2, 3)) 
