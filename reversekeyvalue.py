arr = list(map(int, input().split()))
freq = {}
for key in arr:
    freq[key] = freq.get(key, 0) + 1
result = []
for key , value in freq.items():
    result.extend([value] * key)
result.sort()
print(result)

"""
      input: 3 3 1 1 1 2
      output: [1, 1, 2, 2, 2, 3]
"""