n = int(input())
d = 0
s = []
while n != -1:
    while d <= n:
        d += 1
        if n % d == 0:
            s.append(d)
    if s[-1] == sum(s)-s[-1]:
        print(n,'= ',end = '')
        for i in range(len(s)-2):
            print(s[i],'+ ', end = '')
        print(s[-2])
    else:
        print(f"{n} is NOT perfect.")
    s = []
    d = 0
    n = int(input())
