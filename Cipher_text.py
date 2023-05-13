# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def caesar(text,shift,direction):
#     if direction == "decode":
#         shift *= -1
#     actual_text = ""
#     for letetrs in text:
#         positon = alphabet.index(letetrs)
#         new_position = positon + shift
#         actual_text += alphabet[new_position]
#     print(f"the {direction}d text is {actual_text}")
# caesar(text=text,shift=shift,direction=direction)


# def encryprt(plain_text,shift_amount):
#     cipher_text = ""
#     for letter in text:
#         positon = alphabet.index(letter)
#         new_position = positon + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the encoded text is {cipher_text}")
        

# def decrypt(cipher_text,shift_amount):
#     plain = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain += alphabet[new_position]
#     print(f"the decoded text is {plain}")

# if direction == "encode":
#     encryprt(plain_text=text,shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text,shift_amount=shift)
# else:
#     print("please choose the correct word")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char

    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
import art 
print(art)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_cont = True
while should_cont:

 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
 shift = shift % 26
 caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
 result = input("please type 'yes'to continue and 'no' to end.").lower()
 if result == "no":
   should_cont = False 
   print("good bye")