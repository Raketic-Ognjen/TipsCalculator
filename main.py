#Task is to make tip calculator
print("Welcome to tip calculator")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount =  bill * tip_as_percent
total_bill = (bill + total_tip_amount) / people
print(f"Each person should pay {total_bill} eur")
