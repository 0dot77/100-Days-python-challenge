# Love Calculator Exercise

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# lower() => lower case로 변환해줌
# count() => 인자로 전달하는 값의 개수를 세어줌

# true / love

# 1. 소문자로 변환하기
name1.lower()
name2.lower()

# 2. true / love 계산하기

# true
name1_t = name1.count('t')
name2_t = name2.count('t')

name1_r = name1.count('r')
name2_r = name2.count('r')

name1_u = name1.count('u')
name2_u = name2.count('u')

name1_e = name1.count('e')
name2_e = name2.count('e')

true_num = name1_t+name1_r+name1_u+name1_e+name2_t+name2_r+name2_u+name2_e

# love

name1_l = name1.count('l')
name2_l = name2.count('l')

name1_o = name1.count('o')
name2_o = name2.count('o')

name1_v = name1.count('v')
name2_v = name2.count('v')

# 생각해보기
# - 단순하게 하나씩 할 게 아니라, String을 전부 우선 더해준 뒤에 값을 계산하는 것은 어떨까?

love_num = name1_l+name1_o+name1_v+name1_e+name2_l+name2_o+name2_v+name2_e

love_score = int(f"{true_num}{love_num}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")




