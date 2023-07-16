alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text,shift_no):
    cipher_text=""
    for i in plain_text:
        position=alphabet.index(i)
        new_position=position+shift_no
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print("The encrypted message is : "+cipher_text) 
def decrypt(cipher_text,shift_back):
    decrypt_text=""
    for i in cipher_text:
        position=alphabet.index(i)
        new_position=position-shift_back
        new_letter=alphabet[new_position]
        decrypt_text+=new_letter
    print("The decrypted message is : "+decrypt_text)
if direction=="encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)
