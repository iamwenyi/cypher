tryagain = "True"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while tryagain == "True":
    def cipher(direction,text,shift):
        
        for i in range(0,len(text)):
            if text[i] in alphabet:
                letter_in_text = alphabet.index(text[i])
        
                if direction == "encode":
                    letter_position = letter_in_text + shift
                elif direction == "decode":
                    letter_position = letter_in_text - shift
                else:
                    print("Are you blind? Karen is running to you at a rapid pace of 300 miles per hour. Start running.")
            
                letter_position = letter_position % 26
                new_letter = alphabet[letter_position]
                text = text[0:i] + new_letter + text[i+1:len(text)]
        print(text)
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(direction,text,shift)
    
    tryagain_user = input("Do you want to try again? Yes or no:\n").lower()
    if tryagain_user == "yes":
        tryagain = "True"
    elif tryagain_user == "no":
        tryagain = "False"
        print("Bye")
    else:
        tryagain = "False"
        print("I am very strict. If you don't answer 'yes' it is a no.")