#A drone can fly only if:Battery level is ≥ 60% Weather is clear (boolean) GPS signal is strong (boolean)

battery = int(input("Enter battery level (%): "))
weather_clear = input("Is weather clear? (yes/no): ").lower() == "yes"
gps_strong = input("Is GPS signal strong? (yes/no): ").lower() == "yes"

if battery >= 60 and weather_clear and gps_strong:
    print("Drone can fly.")
else:
    print("Drone cannot fly.")
