# Love Calculator Exercise

# π¨ Don't change the code below π
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# π¨ Don't change the code above π

#Write your code below this line π

# lower() => lower caseλ‘ λ³νν΄μ€
# count() => μΈμλ‘ μ λ¬νλ κ°μ κ°μλ₯Ό μΈμ΄μ€

# true / love

# 1. μλ¬Έμλ‘ λ³ννκΈ°
name1.lower()
name2.lower()

# 2. true / love κ³μ°νκΈ°

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

# μκ°ν΄λ³΄κΈ°
# - λ¨μνκ² νλμ© ν  κ² μλλΌ, Stringμ μ λΆ μ°μ  λν΄μ€ λ€μ κ°μ κ³μ°νλ κ²μ μ΄λ¨κΉ?

love_num = name1_l+name1_o+name1_v+name1_e+name2_l+name2_o+name2_v+name2_e

love_score = int(f"{true_num}{love_num}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")




