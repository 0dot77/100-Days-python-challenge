# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

""" string의 길이를 측정해서 대입하는 방식
peoples_num = len(names)
gen_random = random.randint(0,peoples_num-1)
"""

# 바로 리스트에서 랜덤한 아이템을 선택해준다.
gen_peoples = random.choice(names)

print(f"{gen_peoples} is going to buy the meal today!")

