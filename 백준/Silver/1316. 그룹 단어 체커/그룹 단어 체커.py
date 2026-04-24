n = int(input())
s = n
switch = []
for i in range(n):
    lst = []
    word = list(input())
    for i in range(len(word)):
        if i >= 1 and word[i-1] != word[i] and word[i] in lst:
            switch.append(1)
        else:
            lst.append(word[i])
            switch.append(0)
    if 1 in switch:
        s -= 1
        switch = []
print(s)