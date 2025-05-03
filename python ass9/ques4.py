#Write a function calculate_simple_interest(principal, rate, time) that calculates and returns simpleinterest using the formula:Simple Interest = (Principal × Rate × Time) / 100

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Simple Interest:", calculate_simple_interest(1000, 5, 2)) 
