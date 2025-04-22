#Fuel EAiciency Advisor:Check if a car is fuel eAicient using: mileage >= 18 AND engine_capacity <= 1500cc

mileage = float(input("Enter mileage (km/l): "))
engine_capacity = int(input("Enter engine capacity (cc): "))

if mileage >= 18 and engine_capacity <= 1500:
    print("Car is fuel efficient.")
else:
    print("Car is not fuel efficient.")
