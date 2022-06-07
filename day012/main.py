# scope

# Modifying Global Scope

# enemies = 1


# def increase_enemies():
#     print(f"enemies inside function: {enemies}")  # 2
#     return enemies + 1


# increase_enemies()
# print(f"enemies outside function: {enemies}")  # 1

# Local Scope


# def drink_potion():
#     # 지역 범위 local scope
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()  # 2

# Global Scope
# 파일 내부 어디에서든 사용할 수 있다.
# player_health = 10


# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()


# print(player_health)

# There is no Block Scope

# game_level = 3


# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]

#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)


# create_enemy()

# Global Constants

PI = 3.14159
