from collections import Counter
def frequencysort(s):
    d=Counter(s)
    s_d=sorted(d.items(),key=lambda x:x[1])
    result=" "
    for key , value in s_d:
        result+=key*value
    return result
s=input()
print(frequencysort(s))

#Input:tree
#Output:  rtee