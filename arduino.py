def farthest_pos(A):
    Pos=0
    max_pos=0
    for i in range(len(A)):
        Pos+=A[i]
        max_pos=max(max_pos,Pos)
    return max_pos
A=list(map(int,input().split()))
print(farthest_pos(A))