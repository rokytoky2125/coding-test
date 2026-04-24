n = int(input())

for j in range(1, n+1):
    print(' ' * (n-j) , end = '')
    print('*' * j + '*' * (j-1))