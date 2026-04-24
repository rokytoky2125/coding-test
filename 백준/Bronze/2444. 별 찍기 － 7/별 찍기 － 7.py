n = int(input())

for i in range(1,n+1):
    print(" "*((n)-i)+"*"*i+"*"*(i-1))
for j in range(n,1,-1):
    print(" "*(n-(j-1))+"*"*(j-1)+"*"*(j-2))
