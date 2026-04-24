N = int(input())
han = []


for i in range(1, N+1): #브루트 포스
    if i < 100:
        han.append(i)
    else:
        if int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
            han.append(i)


print(len(han))
