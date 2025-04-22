#Temperature Monitoring System:Check if a machine's temperature is:Below 40°C → Normal Between 40°C to 70°C → Warning Above 70°C → Danger 
temp = float(input("Enter temperature (°C): "))
if temp < 40:
    print("Normal")
elif 40 <= temp <= 70:
    print("Warning")
else:
    print("Danger")
