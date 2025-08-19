# Diwali Contest Problem Solver - approach 1

def diwali_contest(N , P):
    totaltime = 240 -P
    problemsolved=0
    for i in range(1,N+1):
        if totaltime >= 5*i:
            problemsolved += 1
            totaltime -= 5*i
        else:
            break
    return problemsolved
N= int(input())     # number of problems in the contest
P =int(input())    # time taken to reach the contest 
print(diwali_contest(N, P))

# Approach 1: Greedy Method
# This approach iteratively checks how many problems can be solved within the remaining time.
# It starts with the first problem and continues until the time runs out or all problems are solved.
# The time taken for each problem increases linearly (5 minutes for the first, 10 for the second, etc.).
# This is a simple and efficient solution for the problem.
# Example usage:
# Input:
# 5
# 30
# Output:
# 4
def diwali_contest(N, P):
    totaltime = 240 - P
    timespent = 0
    problemsolved = 0
    for i in range(1, N + 1):
        timerequired = 5 * i
        if timespent+ timerequired <= totaltime:
            timespent += timerequired
            problemsolved += 1
        else:
            break
    return problemsolved
N = int(input())  # number of problems in the contest
P = int(input())  # time taken to reach the contest
print(diwali_contest(N, P))