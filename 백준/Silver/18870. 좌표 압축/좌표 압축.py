import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

sorted_value = sorted(set(numbers))

dic = {}
idx = 0
for i in sorted_value:
    dic[i] = idx
    idx += 1

for i in range(n):
    numbers[i] = dic[numbers[i]]
print(*numbers)
