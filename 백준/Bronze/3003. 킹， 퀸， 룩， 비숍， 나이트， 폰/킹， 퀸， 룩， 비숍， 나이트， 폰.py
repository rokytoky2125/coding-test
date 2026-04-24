s=list(map(int,['1','1','2','2','2','8']))
d=[]
n=input().split()
for i in range(len(n)):
    n[i]=int(n[i])
    step=s[i]-n[i]
    d.append(step)
b=' '.join(map(str, d))
print(b)