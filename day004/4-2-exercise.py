# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# π¨ Don't change the code above π

#Write your code below this line π

import random

""" stringμ κΈΈμ΄λ₯Ό μΈ‘μ ν΄μ λμνλ λ°©μ
peoples_num = len(names)
gen_random = random.randint(0,peoples_num-1)
"""

# λ°λ‘ λ¦¬μ€νΈμμ λλ€ν μμ΄νμ μ νν΄μ€λ€.
gen_peoples = random.choice(names)

print(f"{gen_peoples} is going to buy the meal today!")

