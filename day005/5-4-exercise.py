# Fizz Buzz Exercise

# 3 = Fizz
# 5 = Buzz
# 3 & 5 = FizzBuzz

#내 풀이
for n in range(1, 101):
    if n % 3 == 0 and n % 15 != 0:
        print("Fizz!")
    elif n % 5 == 0 and n % 15 != 0:
        print("Buzz!")
    elif n % 15 == 0:
        print("FizzBuzz!")
    else:
        print(n)
        
#쌤 풀이
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
        
    """
    예외 처리를 한 번에 해주는 방식에 대해서 상상해보기
    내 풀이의 경우에는 15를 먼저 상정해서 값을 계산했는데,
    손쉽게 3과 5의 곱의 결과를 먼저 조건문으로 거르고 시작하면
    훨씬 손쉽게 만들 수 있다.
    """