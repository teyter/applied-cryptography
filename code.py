with open('source.txt') as file:
    lines = [line.rstrip() for line in file]
file.close() 
src = " ".join(lines)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " # included whitespace at the end
key = 3

def ensesar(text):
    print("text to encipher:", text, "\n")
    text = text.upper()
    cipher = ""
    for i in text:
        cipher += alphabet[(alphabet.find(i)+key)%len(alphabet)]
    print("enciphered text:", cipher, "\n")
    return cipher

def desesar(cipher):
    print("text to decipher:", cipher, "\n")
    cipher = cipher.upper()
    text = ""
    for i in cipher:
        text += alphabet[(alphabet.find(i)-key)%len(alphabet)]
    print("deciphered text:", text, "\n")
    return text

desesar(ensesar(src))