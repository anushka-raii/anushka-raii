 #Elevator Overload Protection:Given the weight of passengers in an elevator, determine:Normal (≤ 500 kg) Overloaded (> 500 kg) check if the number of people > 8, issue a capacity warning.

weight = float(input("Enter total weight (kg): "))
people = int(input("Enter number of people: "))

if weight <= 500:
    print("Normal")
else:
    print("Overloaded")

if people > 8:
    print("Warning: Exceeds people capacity!")
