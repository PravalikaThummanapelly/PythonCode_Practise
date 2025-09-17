def reverse_words(s):
    words=s.split()
    rev_words=words[::-1]
    return ' '.join(rev_words)
s= input()
print(reverse_words(s))