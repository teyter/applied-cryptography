with open('dracula.txt') as file:
    lines = [line.rstrip() for line in file]
file.close() 
src = " ".join(lines)

from collections import defaultdict

freq = defaultdict(int)

for i in "".join(src.split()):
  if i.isalnum(): # filter out symbols
    freq[i.upper()] += 1

print(freq.items())