#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# 1. Randomly choose a word from the word_list
# 2. assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# 1. Ask the user to guess a letter
# 2. assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter!').lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if guess == letter:
        print('Right')
    else:
        print('Wrong')
