n=input().split()
for i in range(len(n)):
    n[i]=int(n[i])
a=n[0]
b=n[1]
c=n[2]
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)