# Approach:1
def encoded_string(N):
    encoded =""
    for digit in str(N):
        square=int(digit)**2
        encoded+=str(square)
    return int(encoded)
N=int(input())
print(encoded_string(N))