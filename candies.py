def candies():
    N, K, A= map(int,input().split())
    lastchild=(A+K-1)%N
    if lastchild==0:
        lastchild=N
    return lastchild
print(candies())