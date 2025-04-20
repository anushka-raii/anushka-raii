#Calculator After eating out, your total bill is ₹1850. You want to tip 12.5%. Write a program to calculate the tip amount and total amount payable.

bill = 1850
tip_percent = 12.5
tip = bill * tip_percent / 100
total = bill + tip

print("Tip: ₹", tip)
print("Total Amount: ₹", total)
