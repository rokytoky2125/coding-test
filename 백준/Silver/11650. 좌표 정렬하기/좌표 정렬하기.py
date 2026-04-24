n = int(input())
lst = []
for i in range(n):
    nums = list(map(int, input().split()))
    lst.append(nums)
    
lst.sort()

for i in lst:
    print(*i)
