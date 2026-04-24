def convert(n, b):
    if n == 0:
        return '0'
    string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    while n > 0:
        result.append(string[n % b])
        n = n // b
    return ''.join(reversed(result))
n, b = map(int, input().split())
s = convert(n, b)
print(s)