def max_subarray(n,num):
    max_sum=num[0]
    current_sum=num[0]
    for i in range(1,n):
        current_sum=max(num[i],current_sum+num[i])
        max_sum=max(max_sum,current_sum)
    return max_sum
n=int(input())
num=list(map(int,input().split()))
print(max_subarray(n,num))