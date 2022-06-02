# Blind-Action

import os;
from art import logo

print(logo)

# 키와 값을 사용해서 경매 시스템을 만들어보기
bid_data = []

is_another_bidder = False
while not is_another_bidder:
# 1. 이름 묻기
    user_name = input("What is your name?").lower()

# 2. 얼마를 걸거니?
    user_bid = input("What is your bid? $")
    
# 3. 또 걸 사람 있음?
    another_user = input("Are there any bidders? Type 'yes or no'").lower()
    
# 여기까지 도달했을 떄 함수로 딕셔너리에 값 넣어주기?
    def add_new_user(name, bid):
        new_user = {}
        new_user["name"] = user_name
        new_user["bid"] = user_bid
        bid_data.append(new_user)
    
    add_new_user(user_name, user_bid)
    
# 3. 다른 투자자가 있는지 묻기 -> 조건문
    if another_user == 'no':
        is_another_bidder = True
# 3-2 없다면, 가장 많이 건 사람 찾기
        find_highest_bid = []
        for user in bid_data:
            find_highest_bid.append(user["bid"])
        print(max(find_highest_bid))
# 3-1 있다면, 1로 돌아가기
    else:
        os.system("clear")
    
