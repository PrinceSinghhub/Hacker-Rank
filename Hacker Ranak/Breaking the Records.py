x=int(input())
score = list(map(int,input().split()))

Max = []
Min = []
ms = 0
maxs = 0
for i in score:
    if len(Max) == 0 and len(Min) == 0:
        Max.append(i)
        Min.append(i)

    if len(Max) and len(Min) > 0:
        for m in Max:
            if i > Max[len(Max)-1]:
                Max.append(i)
                maxs += 1


        for n in Min:
            if i < Min[len(Min)-1]:
                Min.append(i)
                ms += 1
print(maxs,ms)


