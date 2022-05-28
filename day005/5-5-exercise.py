# Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

""" 나의 풀이
# index를 활용해서 루프 돌리기

result_letters = ""
result_symbols = ""
result_numbers = ""

for n in range(0, nr_letters):
    result_letters += letters[random.randint(0,len(letters))]
    
for n in range(0, nr_symbols):
    result_symbols += numbers[random.randint(0,len(symbols))]
    
for n in range(0, nr_numbers):
    result_numbers += symbols[random.randint(0,len(numbers))]

print(f"Easy Version : {result_letters}{result_symbols}{result_numbers}")


#1. random.sample()을 활용해서 인덱스를 섞었는데, 다른 방법이 무엇이 있을까?
#2. 왜 자꾸 index error가 발생하는 지 모르겠음. 난수를 발생시킬 때의 오류일까?

    
result_random = result_letters +result_symbols +result_numbers;
hard_version = random.sample(result_random, len(result_random))
print(f"Hard version : {''.join(hard_version)}")

"""

# 생각해보기 
# - 루프에 사용하는 값을 꼭 사용하지 않아도 된다. (반복을 도는 횟수를 저장하는 값)
# - 사용해야 한다는 강박이 랜덤한 값을 추출하는 배열의 범위를 정하게 했다.

""" 선생님 풀이
"""
# password = ""

# for char in range(1, nr_letters + 1):
#     # 반복문을 돌면서 리스트에서 랜덤한 문자열을 추출해준다.
#     # 배열에서 랜덤한 값을 계속해서 추출하는 것이다. 따라서 사용자가 값을 몇을 입력하더라도 index error가 발생하지 않는다.
#     password += random.choice(letters) 

# for char in range(1, nr_symbols):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers):
#     password += random.choice(numbers)
    
# print(password)

# Hard mode
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
    
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}")