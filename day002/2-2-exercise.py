# BMI Calculator Exercise

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = float(weight) / float(height) ** 2;
bmi_as_int = int(bmi);
print("Your BMI is : " + str(bmi_as_int))


