x = int(input())
y = int(input())

def q():
    n = 0
    if x > 0:
        if y > 0:
            n = 1
        else:
            n = 4
    else:
        if y > 0:
            n = 2
        else:
            n = 3
    return n

n = q()
print(n)