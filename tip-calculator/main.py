print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

result = (float(bill) / int(people)) * (1 + int(tip) / 100)
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")
