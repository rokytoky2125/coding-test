n = int(input())
lst = []

while n > 1:
    for i in range(2, n+1):
        if n % i == 0:
            lst.append(i)
            n = n // i
            break
for i in lst:
    print(i)
