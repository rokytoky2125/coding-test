n_b = input().split()
n = n_b[0]
b = int(n_b[1])
s = len(n)-1
result = 0

for i in range(len(n)):
    if ord('A') <= ord(n[i]) <= ord('Z'):
        value = ord(n[i]) - ord('A') + 10
    else:
        value = int(n[i])
    result += value * (b**s)
    s -= 1
print(result)