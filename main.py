#Task is to make tip calculator
print("Welcome to tip calculator")
bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
people = input("How many people to split the bill?\n")

total_bill = (float(bill) + ((float(bill)*int(tip))/100)) / int(people)
print(f"Each person should pay {total_bill} eur")
