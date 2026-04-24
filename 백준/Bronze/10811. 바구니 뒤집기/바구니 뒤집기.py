n, m = map(int, input().split()) #바구니 개수, 역순으로 바꾸는 횟수
lst = list(range(1, n+1))
for i in range(m):
    a, b = map(int, input().split()) #범위, 순서
    lst[a-1:b] = lst[a-1:b][::-1]
    
print(*lst)
