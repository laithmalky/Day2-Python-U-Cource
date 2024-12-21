
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15 ? "))
people = int(input("How many people to split the bill? "))


#n = (bill / people) * (tip / 100 + 1)
tip_prc = tip / 100 
total_bill = (tip_prc + 1) * bill
pay_per_person = total_bill / people

print(f"Each person should pay: ${round(pay_per_person, 2)}")
#print(f"Each person should pay: ${round(n, 2)}")
