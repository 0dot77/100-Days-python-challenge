from data import MENU, resources
import random

# Espresso, Latte,
# Penny 0,01, Dime 0.10, Nickel 0.05, Quarter 0.25
# requirements
# 1. print report.
# 2. Check resources sufficient?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee

# 기계가 꺼져있는지 켜져있는지 체크하기
machine_off = False

# 각 리소스 초기화
milk = resources["milk"]
water = resources["water"]
coffee = resources["coffee"]
## 돈은 랜덤하게 가지고 있을 수 있도록 하기
money = random.randint(1, 300)


def machine_report():
    # 현재 남아있는 리소스를 출력하기
    print(f"Milk: {milk}ml")
    print(f"Water: {water}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def machine_check(coffee_name):
    ingredients = MENU[coffee_name]["ingredients"]

    if (
        water >= ingredients["water"]
        and milk >= ingredients["milk"]
        and coffee >= ingredients["coffee"]
    ):
        return True
    else:
        return False


def calculate_coins(quarters, dimes, nickles, pennies):
    sum = (
        float(quarters) * 0.25
        + float(dimes) * 0.10
        + float(nickles) * 0.05
        + float(pennies) * 0.01
    )
    print(f"총합 : {sum}")
    return sum


def makeCoffee(choiced_coffee):
    from_ingredients = MENU[choiced_coffee]["ingredients"]
    from_money = MENU[choiced_coffee]["cost"]

    print("---Before make coffee---")
    machine_report()
    print("---After make coffee---")
    print(
        f'Milk: {milk - from_ingredients["milk"]}ml\nWater: {water - from_ingredients["water"]}ml\nCoffee: {coffee - from_ingredients["coffee"]}g\nMoney: ${money-from_money}'
    )
    print("Here is your latte. Enjoy!")


def main(choice):
    selected_coffee = choice

    if machine_check(selected_coffee):
        print("Please Insert your Coins")
        quarter = input("Quarters?")
        dimes = input("Dimes?")
        nickel = input("Nickels?")
        pennies = input("Pennines?")
        user_insert_coin = calculate_coins(quarter, dimes, nickel, pennies)

        if user_insert_coin == MENU[selected_coffee]["cost"]:
            makeCoffee(selected_coffee)

        elif user_insert_coin > MENU[selected_coffee]["cost"]:
            # 돈이 넘치면 돈을 거슬러준다.
            print(
                f"Here is ${user_insert_coin - MENU[selected_coffee]['cost']} dollars in change."
            )
            makeCoffee(selected_coffee)
        else:
            print("Sorry that's not enough money. Money refunded.")
            return


while not machine_off:
    user_choice = input("What would you like? (Espresso/Latte/cappuccino)")
    # bool 체크를 하면서 기계의 기능들을 넘어가는 방식을 사용하기 -> 다시 작성해보기
    # 1. 커피 입력하기
    # 1-1 입력이 틀리면, 다시 입력 요청
    # 1-2 입력이 맞으면 2로 이동
    # 2. 기계 점검
    # 2-1 모든 재료가 커피에 맞게 있으면 다음 단계로 이동
    # 2-2 없다면 없는 항목에 맞춰서 출력
    # 3. 코인
    # 3-1 코인을 넣으라 요청, 각각의 동전을 요구, 충분하면 커피를 뽑음과 동시에 리포트 제공
    # 3-2 충분하지 않으면 돈 없다고
    # 4. 커피 만들기
    # 4-1

    # report
    if user_choice == "report":
        machine_report()
    elif user_choice == "espresso" or "latte" or "cappuccino":
        main(user_choice)
        break
    elif user_choice == "off":
        break
