# TIP Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip Calcualtor!")
bill = input("What was the total bill?")
tip = input("How much tip would you like to give? 10, 12, or 15?")
peoples = input("How many people to split the bill?")

calc_bill = float(bill)
calc_tip = int(tip) * 0.01
calc_peoples = int(peoples)
calc_each_people = calc_bill / calc_peoples

calc_each_people_tips = (calc_bill / calc_peoples) * calc_tip
result_calc = round(calc_each_people_tips + calc_each_people, 2)

result = f"Each person should pay: ${result_calc}"
print(result)
