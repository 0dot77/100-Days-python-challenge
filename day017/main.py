class User:
    def __init__(self, user_id, user_name):
        print("new user being created...")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.following += 1
        self.following += 1

    pass


user_1 = User("001", "taeyang")
print(user_1.username)
print(user_1.followers)

user_2 = User("002", "angela")
user_2.id = "002"
print(user_2.id)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
