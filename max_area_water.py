#Approach:1   Brute Force            TC: O(n^2)  ,SC: O(1)
def max_area(arr):
    n=len(arr)
    max_area=0
    for i in range(n):
        for j in range(i+1,n):
            area=min(arr[i],arr[j])*(j-i)
            max_area=max(max_area,area)
    return max_area
arr=list(map(int,input().split()))
print(max_area(arr))

#approach:2     Two-Pointer TC: O(n), SC: O(1)
def max_area(arr):
    n=len(arr)
    left=0
    right=n-1
    max_area=0
    while left<right:
        area=min(arr[left],arr[right])*(right-left)
        max_area=max(max_area,area)
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    return max_area
arr=list(map(int,input().split()))
print(max_area(arr))