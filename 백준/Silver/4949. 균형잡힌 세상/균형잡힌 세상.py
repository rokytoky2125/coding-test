def vps(ps):
    stack = []
    for i in ps:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                return 'no'
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                return 'no'
            stack.pop()
    return 'yes' if not stack else 'no'

while True:
    n = input()
    if n == '.':
        break
    print(vps(n))
