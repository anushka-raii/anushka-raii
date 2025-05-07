# Sum of Even Numbers in a Range

def sum_of_evens(start, end):
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:  
            total += number
    return total

print("Sum of even numbers from 1 to 10 is:", sum_of_evens(1, 10))  
