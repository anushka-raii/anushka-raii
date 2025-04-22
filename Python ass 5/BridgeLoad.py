#Given the total weight on a bridge (in tons), issue warnings based on:Safe if < 20 tons ,Caution if 20-30 tons, Danger if > 30 tons

weight = float(input("Enter total weight on bridge (tons): "))
if weight < 20:
    print("Safe")
elif 20 <= weight <= 30:
    print("Caution")
else:
    print("Danger")
