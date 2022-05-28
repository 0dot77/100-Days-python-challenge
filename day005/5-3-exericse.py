# Adding Evens Exercise


#1
total_evens = 0
for number in range(1,101,2):
    total_evens += number+1
print(total_evens)

#2
total_evens_2 = 0
for number in range(2,101,2):
    total_evens_2 += number
print(total_evens_2)

#3
total_evens_3 = 0
for number in range(1,101):
    if number % 2 == 0:
        total_evens_3 += number
print(total_evens_3)