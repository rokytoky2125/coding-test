a, b, c = map(int, input().split())
nums = [a, b, c]

if a == b and b == c:
    p = 10000 + a*1000
elif a == b or b == c or c == a :
    if a == b:
        p  = 1000 + a*100
    elif b == c:
        p = 1000 + b*100
    elif c == a:
        p = 1000 + c*100
else:
    p = max(nums)*100

print(p)