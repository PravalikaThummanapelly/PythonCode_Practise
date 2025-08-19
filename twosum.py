# Function to find two indices such that their corresponding values sum up to the target
# This implementation uses a brute force approach with O(n^2) time complexity

# def twosum(nums,target):
#     n= len(nums)
#     for i in range(n):
#         for j in range(1 , n):
#             if nums[i] +nums[j] == target:
#                 return [i , j]
#     return None 
# nums = list(map(int,input().split()))
# target = int(input()) 
# print(twosum(nums, target))       

#Approach 2: Using a dictionary to achieve O(n) time complexity
def twosum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None
nums = list(map(int,input().split()))
target = int(input()) 
print(twosum(nums, target)) 