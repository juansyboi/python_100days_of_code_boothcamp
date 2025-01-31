print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_ppl = int(input("How many people to split the bill? "))

tip_formula = tip / 100
final_bill = round((bill + (bill * tip_formula)) / num_ppl, 2)

print(final_bill)
