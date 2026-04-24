import sys
input = sys.stdin.readline

n = int(input())
stack = []
output = []

for i in range(n):
    order = input()
    if order.startswith('push'):
        stack.append(order.split()[1])
    elif order.startswith('pop'):
        if stack:
            output.append(stack.pop())
        else:
            output.append('-1')
    elif order.startswith('size'):
        output.append(str(len(stack)))
    elif order.startswith('empty'):
        output.append('0' if stack else '1')
    elif order.startswith('top'):
        output.append(stack[-1] if stack else '-1')
        
print('\n'.join(output))
        
