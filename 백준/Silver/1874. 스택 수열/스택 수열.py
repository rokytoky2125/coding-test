n = int(input())
sample = [int(input()) for _ in range(n)]
stack = []
result = []
ret = []

cnt = 0
check = 0
possible = True

while sample != result:
    if stack:
        if sample[check] == stack[-1]:
            result.append(stack.pop())
            check += 1
            ret.append('-')
        else:
            cnt += 1
            if cnt > n:
                possible = False
                break
            stack.append(cnt)
            ret.append('+')
    else:
        cnt += 1
        if cnt > n:
            possible = False
            break
        stack.append(cnt)
        ret.append('+')
        
if possible:
    for i in ret:
        print(i)
else:
    print('NO')
