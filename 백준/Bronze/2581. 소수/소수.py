m = int(input())
n = int(input())
lst = [] #i의 약수들(=j)
lst_result = [] #i의 약수가 2개인 i(=소수)

for i in range(m, n+1):
    for j in range(1, i+1):
        if i % j == 0:
            lst.append(j)
    if len(lst) == 2:
        lst_result.append(i)
    lst = []
if len(lst_result) == 0:
    print(-1)
else:
    print(sum(lst_result))
    print(min(lst_result)) 
