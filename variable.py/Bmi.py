
#Description:Ask the user to input their weight (kg) and height (meters). Calculate and display the Body Mass 
#Formula:BMI = weight / (height * height)
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
print("Your BMI is:", round(bmi, 2))
