print("Welcome to the tip calculator.\n")
bill=input("What was the total bill? $")
bill=float(bill)
tip=input("What percentage tip would you like to give?10, 12 or 15? ")
tip="1."+str(tip)
tip=float(tip)
total_bill=bill*tip
people=input("How many people to split the bill? ")
people=int(people)
payment=round(total_bill/people,2)
print(f"Each persone should pay: ${payment}")

