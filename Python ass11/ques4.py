#Handle Division by Zero
def safe_divide():
    try:
        num1 = float(input("Enter numerator: "))
        num2 = float(input("Enter denominator: "))
        result = num1 / num2
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")

safe_divide()

