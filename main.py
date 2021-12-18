
print("Welcome to Bill and Tip Calculator")
n=int(input("Enter total number of people : "))
bill=float(input("Enter the amount of total bill : ₹"))
r = float(input('Enter percentage of tip to be given : '))
tip = bill*r*0.01
amt = bill+tip
each = amt/n
print('The amount to be paid as tip : ₹',round(tip,2))
print('The total amount to be paid is : ₹',round(amt))
print('Amount each person has to pay : ₹',round(each))



