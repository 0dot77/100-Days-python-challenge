# Rock-Paper-Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

# choice list
choice_list = [rock,paper,scissors]

# random gen
gen_random_num = random.randint(0, 2)

# 랜덤 이미지 생성하기
gen_random_choice = choice_list[gen_random_num]

# 유저의 값 받기
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors!"))

if user_choice >= 3 or user_choice < 0:
    print("You typed a invaild number")
else:
    user_choice_num = user_choice
    user_result = choice_list[user_choice_num]
    print(user_result)
    print(gen_random_choice)

    if user_choice_num == gen_random_num:
        print("Draw!")
    # rock 일때
    elif user_choice_num == 0 and gen_random_num == 1:
        print("You lose!")
    elif user_choice_num == 0 and gen_random_num == 2:
        print("You win!")
    elif user_choice_num == 1 and gen_random_num == 0:
        print("You win!")
    elif user_choice_num == 1 and gen_random_num == 2:
        print("You lose!")
    elif user_choice_num == 2 and gen_random_num == 0:
        print("You lose!")
    else:
        print("You win!")