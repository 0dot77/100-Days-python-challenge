# Average Height Exercise

# π¨ Don't change the code below π
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# π¨ Don't change the code above π


#Write your code below this row π

result = 0 # μ μΈμ κΌ­ μ΄λ κ² ν΄μΌν κΉ = γγ μ΄λ κ² ν¨
for height in student_heights:
    result += height
average = round(result/len(student_heights))
print(average)