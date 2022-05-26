# Leap Year Exercise

# 4로 나눴을 때 나머지가 없으면 윤년이다
# 다만 예외로 100으로 나눠지면 윤년이 아니다
# 하지만 해당 해가 400으로 나눠지면 여전히 윤년이다

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")


    
        
    
    