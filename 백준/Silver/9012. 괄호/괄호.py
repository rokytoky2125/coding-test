def vps(ps):
    stack = []
    a = False
    for i in ps:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                print('NO')
                a = True
                break
            else:
                stack.pop()
    if a == False:
        if stack:
            print('NO')
        else:
            print('YES')

        
n = int(input())
for i in range(n):
    ps = list(input())
    vps(ps)
