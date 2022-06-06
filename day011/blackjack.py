from telnetlib import LOGOUT
from art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# 1. 게임 시작을 알려줘야 함

is_game_start = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': "
).lower()

# is_game_run 변수를 활용해서 게임을 시작할 지 그대로 끝낼지 설정해준다.
if is_game_start == "y":
    is_game_run = True
    print(logo)
else:
    is_game_run = False

# 카드 정의하기
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# def playing_game(first):
#     player_cards = []
#     computer_cards_after_first_turn = []
#     computer_final_hands = []
#     if first:
#         # 랜덤한 카드 두장을 뽑아서 플레이어에게 주고
#         #! random.choices(list, k=n) 배열에서 요소를 뽑고 싶은 개수만큼 랜덤으로 뽑아준다.
#         player_cards = random.choices(cards, k=2)
#         # 플레이어의 현재 점수를 합산해준다.
#         player_score = sum(player_cards)
#         # 컴퓨터의 숨겨놓을 final hand 배열을 미리 만들어준다.
#         computer_final_hands = []
#         computer_cards = random.choice(cards)
#         computer_final_hands.append(computer_cards)
#         print(
#             f"Your cards {player_cards}, current score: {player_score}\nComputer's first card: {computer_cards}"
#         )
#     else:
#         # 첫 턴이 아니라면 한 장의 카드씩 랜덤으로 추가해준다.
#         player_cards.append(random.choice(cards))
#         player_score = sum(player_cards)
#         # 첫 턴 이후부터는 컴퓨터가 뽑는 카드는 보여주지 않고, final hand에 집어넣는다.
#         computer_cards_after_first_turn = random.choice(cards)
#         computer_final_hands.append(computer_cards_after_first_turn)
#         print(
#             f"Your cards {player_cards}, current score: {player_score}\nComputer's first card: {computer_cards}"
#         )

# dictionary 사용하기

card_condition = {
    "player_cards": random.choices(cards, k=2),
    "computer_cards": random.choices(cards, k=2),
}

# 결과값을 프린트 해주는 함수 분리해주기
def current_notice(players, score, computers):
    """현재 값을 설명해주기

    Args:
        players (list) : player가 들고 있는 카드 꾸러미
        score (int): player의 현재 스코어 합
        computers (int): 컴퓨터가 가장 처음 뽑아낸 값
    """
    print(
        f"Your cards {players}, current score: {score}\nComputer's first card: {computers}"
    )


def final_notice(players, player_score, computers, computers_score):
    print(
        f"Your final hand: {players}, final score: {player_score}\nComputer's final hand: {computers}, final score: {computers_score}"
    )


# 컴퓨터의 리스트 합이 21이 안될 때 리스트에서 카드를 뽑아내 값을 합해주기
def pick_and_sum(scores):
    computer_pick_card = random.choice(cards)
    scores.append(computer_pick_card)
    return sum(scores)


def player_stop_game(player_scores, computer_scores):
    # 끝낼 때 컴퓨터 카드 합이 21이 안된다면, 더 뽑아서 맞추도록 설계하기
    final_computer_score = sum(computer_scores)

    # 21에 가까워질 때까지 계속 뽑아서 값을 맞추기
    while final_computer_score < 21:
        final_computer_score = pick_and_sum(computer_scores)

    # 최종 결과 출력해주기
    player_cards = player_scores
    player_final_score = sum(player_cards)
    computer_cards = computer_scores
    final_notice(player_cards, player_final_score, computer_cards, final_computer_score)

    if final_computer_score > 21 and player_final_score < 21:
        print("You win ☺️")
    elif player_final_score < final_computer_score:
        print("You lose 🙃")

    if player_final_score > 21:
        print("You lose ❌")
    elif player_final_score > final_computer_score:
        print("You win 👍")


# 게임 진행할 때 계속해서 돌려줄 함수
def player_run_game(player_cards, computer_cards):
    # 해당 턴의 유저 카드 리스트 구성
    player_pick_new_card = random.choice(cards)
    player_cards.append(player_pick_new_card)
    player_current_score = sum(player_cards)
    # 내 카드의 합이 21이 넘어가면
    if player_current_score > 21:
        player_stop_game(player_cards, computer_cards)
    # current_notice(
    #     card_condition["player_cards"],
    #     sum(card_condition["player_cards"]),
    #     card_condition["computer_cards"][0],
    # )


while is_game_run:
    # 초기 값 보여주기
    print(
        f"Your cards {card_condition['player_cards']}, current score: {sum(card_condition['player_cards'])}\nComputer's first card: {card_condition['computer_cards'][0]}"
    )

    # 게임을 계속 할지 말지 설정하기
    is_keep_playing_game = input(
        "Type 'y' to get another card, type 'n' to pass: "
    ).lower()

    if is_keep_playing_game == "n":
        player_stop_game(
            card_condition["player_cards"], card_condition["computer_cards"]
        )
        is_game_run = False
    else:
        card_condition["computer_cards"].append(random.choice(cards))
        player_run_game(
            card_condition["player_cards"], card_condition["computer_cards"]
        )
