# Average Height Exercise

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

result = 0 # 선언을 꼭 이렇게 해야할까 = ㅇㅇ 이렇게 함
for height in student_heights:
    result += height
average = round(result/len(student_heights))
print(average)