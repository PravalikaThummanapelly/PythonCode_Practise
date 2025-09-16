#Approach:1
from collections import Counter
def frequencySort(s):
    freq=Counter(s)
    max_freq=max(freq.values())
    return len(s)-max_freq
s=input()
print(frequencySort(s))


#Approach:2
def magic_number(s):
    freq={}
    for char in s:
        freq[char]=freq.get(char , 0)+1
    max_freq=max(freq.values())
    return len(s) - max_freq
s=input()
print(magic_number(s))