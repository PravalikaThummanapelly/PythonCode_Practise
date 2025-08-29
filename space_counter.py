def space_counter(s):
    count=0
    i=0
    while i<len(s):
        if s[i] == ' ' and i>0 and i<len(s)-1:
            if s[i-1] != ' ' and s[i+1] != ' ':
                count+=1
        i+=1
    return count
s=input()
print(space_counter(s))