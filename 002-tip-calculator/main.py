print('Welcome to the tip calculator')
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
guests = int(input("How many people to split the bill? "))

tip = bill * tip_percentage / 100
full_bill = bill + tip
charge_per_person = round(full_bill / guests, 2)

print(f"Each person should pay: ${charge_per_person}")