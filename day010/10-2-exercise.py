# Calculator Project
from art import logo

# Add


def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Muliply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

# 재귀적으로 작동하는 함수 만들기
def calculator():
    # TODO: while을 사용해서 계산기의 계산을 지속 하고 싶다면 계속해서 계산을 할 수 있도록 한다.
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    is_calc_over = False

    while not is_calc_over:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        isOver = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: "
        ).lower()

        if isOver == "n":
            is_calc_over = True
            calculator()
        else:
            num1 = answer


calculator()
