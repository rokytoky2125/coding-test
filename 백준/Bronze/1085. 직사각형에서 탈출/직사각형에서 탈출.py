x, y, w, h = map(int, input().split())
a = h - y
b = w - x
c = x
d = y
lst = [a, b, c, d]
print(min(lst))
