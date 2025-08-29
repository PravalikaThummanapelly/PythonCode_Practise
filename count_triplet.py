#Approach : brute force    T.C:O(n^3)
#                            S.C:O(1)

def count_triplet(arr,m):
    n=len(arr)
    count =0
    unique_triplet = set()
    for i in range(n):
        for j in range(i+1 , n):
            for k in range(j+1 , n):
                if arr[i] * arr[j] * arr[k] == m:
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    unique_triplet.add(triplet)
    return len(unique_triplet)
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
print(count_triplet(arr,m))