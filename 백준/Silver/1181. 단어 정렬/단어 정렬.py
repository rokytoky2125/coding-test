n = int(input())
lst = []
for i in range(n):
    voc = input()
    if voc not in lst:
        lst.append(voc)

lst.sort(key = lambda x: (len(x), x))
for i in lst:
    print(i)
