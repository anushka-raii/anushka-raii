#Write a function print_table(number, limit) that prints the multiplication table for the given number up to limit.

def print_table(number, limit):
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")
print_table(5, 4)
