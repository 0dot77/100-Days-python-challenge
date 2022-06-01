# Caesar-Cipher-4

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #텍스트가 인코딩/디코딩 될 때 숫자/기호/공백이 유지되도록 하기
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char not in alphabet:
        end_text += char
    else:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
        
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

isRestart = False

while not isRestart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    if shift > 26:
        shift = shift % 26 # 최대 수를 넘어갔을 떄 모듈러를 사용해서 개수를 넘어가지 않도록 해준다.
        

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if restart == 'no':
        isRestart = True
    else:
        print("Bye!")
        isRestart = False