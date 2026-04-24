n, m = map(int, input().split())
hear = set()
see = set()

for i in range(n):
    name = input()
    hear.add(name)

for i in range(m):
    name = input()
    see.add(name)
    
result = hear & see

print(len(result))
for i in sorted(result):
    print(i)
