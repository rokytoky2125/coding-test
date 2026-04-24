n = int(input())
initial = 2

for i in range(n):
    result = (initial + (initial - 1))**2
    initial += initial - 1
print(result)