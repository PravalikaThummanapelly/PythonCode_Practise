# Diwali Contest Problem Solver - approach 1

def diwali_contest(N , P):
    totaltime = 240 -P   # diwali contest time limit is 240 minutes 
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

# Diwali Contest Problem Solver - approach 2
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