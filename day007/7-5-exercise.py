#Step 5

import random

# import hangman_words
# import hangman_art

# 파일에서 데이터 임포트시키기
from hangman_words import word_list
from hangman_art import stages,logo
# from hangman_art import logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        
        print(f"{guess} is not in the word!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. Try Next time")
    else:
        print(f"{guess} is in the word!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    print(stages[lives])