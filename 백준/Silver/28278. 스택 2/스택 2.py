import sys
input = sys.stdin.readline

n = int(input())
stack = []
output = []

for i in range(n):
    inp = input().split()
    
    if inp[0] == '1':
        stack.append(int(inp[1]))
    elif inp[0] == '2':
        output.append(str(stack.pop()) if stack else '-1')
    elif inp[0] == '3':
        output.append(str(len(stack)))
    elif inp[0] == '4':
        output.append('1' if not stack else '0')
    elif inp[0] == '5':
        output.append(str(stack[-1]) if stack else '-1')

sys.stdout.write('\n'.join(output) + '\n')

