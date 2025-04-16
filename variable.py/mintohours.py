# Convert Minutes to Hours and Minutes.Store total minutes in a variable and convert it to hours and minutes. 

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(total_minutes, "minutes =", hours, "hours and", minutes, "minutes")
