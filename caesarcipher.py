alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def cipher(plain_text,shift_no,shift_direction):
        cipher_text=""
        if(shift_direction=="decode"):
            shift_no*=-1
        for i in plain_text:
            position=alphabet.index(i)
            new_position=position+shift_no  
            cipher_text+=alphabet[new_position]
        print(f"The {shift_direction}d message is : {cipher_text}")
cipher(text,shift,direction)