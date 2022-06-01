# Caesar-Cipher-1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# 1. Create a function called 'encrypt'
# 2.takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    
    # 1.텍스트가 입력이 되어서 함수로 진입한다.
    # 2.진입한 텍스트를 쪼개서 리스트로 저장한다.
    text_to_list = []
    for item in text:
        text_to_list.append(item)
    
    # 3.각 리스트에 해당하는 알파벳을 shift 해준다.
    # alphabet list에서 해당하는 text의 알파벳의 위치값 index를 찾고, 그 index에 shift를 더한 값을 표현해주는 alphabet을 저장해준다.
    
    # 3-1 alphabet list에서 해당하는 text의 알파벳의 위치값 index를 찾고
    # list.index() 사용하기
    origin_pos = []
    
    for text in text_to_list:
        origin_pos.append(alphabet.index(text))

    # 3-2 그 index에 shift를 더한 값을 표현해주는 alphabet을 저장해준다.
    result_text = []
    for pos in origin_pos:
        result_pos = pos + shift
        if result_pos >= len(alphabet):
            result_pos -= len(alphabet)
        result_text.append(alphabet[result_pos])
    
    print("".join(result_text))
    
    # print("".join(result_text))
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text,shift)