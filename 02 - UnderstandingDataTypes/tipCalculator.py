#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

bill = input("What was the total bill? $\n")
bill = float(bill) 
people = input("How many people to split the bill?\n")
people = int(people)
tip = input("What percentage tip would you like to give? 10, 12, or 15?\n")
tip = int(tip) / 100
total_bill = bill * (1 + tip)
each_person = total_bill / people
each_person = round(each_person, 2)
print(f"Each person should pay: ${each_person:.2f}")
