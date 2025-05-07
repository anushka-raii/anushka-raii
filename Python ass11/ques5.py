#Input Type Checker

def get_integer():
    while True:
        try:
            value = int(input("Please enter a valid integer: "))
            print(f"You entered: {value}")
            return value
        except ValueError:
            print("That's not a valid integer. Try again.")

get_integer()
