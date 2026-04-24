n, m = map(int, input().split()) #바구니 개수, 공 바꾸는 횟수
lst = list(range(1, n+1))   
for k in range(m):
    a, b = map(int, input().split())
    lst[a-1], lst[b-1] = lst[b-1], lst[a-1]
print(*lst)