import sys
input = sys.stdin.readline
write = sys.stdout.write

a, b, v = map(int, input().split())
days = (v - b - 1) // (a - b) + 1

        
write(str(days) + '\n')
