class AgeException(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeException("Access denied. Must be 18 or older.")
    else:
        print("Access granted.")

try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
except AgeException as e:
    print(e)
