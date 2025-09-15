from collections import Counter
def frequencySort(s):
    d=Counter(s)
    s_d=sorted(d.items(),key=lambda x:(x[1],-x[0]))
    result=[]
    for key ,value in s_d:
        for i in range(value):
            result.append(key)
    return result
s=list(map(int,input().split()))
frequencySort(s)