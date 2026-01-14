src = "the quick brown fox jumped over the lazy dog"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " # included whitespace at the end

def ensesar(text):
    print("text to encipher:", text)
    key = 3
    text = text.upper()
    cipher = ""
    for i in text:
        cipher += alphabet[(alphabet.find(i)+key)%len(alphabet)]
    print("enciphered text:", cipher)
    return cipher

def brutus(cipher): # et tu, brute?
    print("text to decipher:", cipher)
    cipher = cipher.upper()
    for key in range(len(alphabet)):
        text = ""
        for i in cipher:
            text += alphabet[(alphabet.find(i)-key)%len(alphabet)]
        print("key:", key, "=", text)

brutus(ensesar(src))