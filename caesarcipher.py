import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
j="yes"
while j!="no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    def cipher(plain_text,shift_no,shift_direction):
        cipher_text=""
        if(shift_direction=="decode"):
            shift_no*=-1
        for i in plain_text:
            if i in alphabet:
                position=alphabet.index(i)
                new_position=position+shift_no  
                cipher_text+=alphabet[new_position]
            else:
                cipher_text+=i
        print(f"The {shift_direction}d message is : {cipher_text}")
    cipher(text,shift,direction)
    j=input("Do you want to start again (yes/no) : ").lower()