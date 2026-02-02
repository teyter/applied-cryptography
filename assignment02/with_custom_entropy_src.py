import time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ " # included whitespace at the end

def letter2number(c):
    return alphabet.find(c.upper())

def number2letter(n):
    return alphabet[n]

def genkey(c):
    return int(time.clock_gettime_ns(time.CLOCK_MONOTONIC)) % len(alphabet)

txt = "the quick brown fox jumped over the lazy dog"

# encrypt
keys = []
kuber = "" # empty string to build the cipher
for c in txt:
    key = genkey(c)
    keys.append(key)
    kuber += number2letter((letter2number(c) + key) % len(alphabet))
print(kuber)
print(keys)

# decrypt
ds = "" # decrypted string
for i in range(len(kuber)):
    ds += number2letter((letter2number(kuber[i]) - keys[i]) % len(alphabet))
print(ds)
