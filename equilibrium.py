def equilibrium_index(A,N):
    total_sum=sum(A)
    left_sum=0
    for i in range(N):
        total_sum-=A[i]
        if left_sum==total_sum:
            return i+1
        left_sum +=A[i]
    return "NOT FOUND"
N=int(input())
A=list(map(int,input().split()))
print(equilibrium_index(A,N))