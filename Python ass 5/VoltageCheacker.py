#Voltage Checker:Given a voltage reading from a sensor, check if the voltage is within safe limits (between 210V and 250V). If not, print a warning. 
voltage = float(input("Enter voltage (V): "))
if 210 <= voltage <= 250:
    print("Voltage is within safe limits.")
else:
    print("Warning: Voltage out of safe range!")
