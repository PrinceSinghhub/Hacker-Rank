n = int(input())
choco = list(map(int,input().split()))
d,m = map(int,input().split())

sep_seg = []
s=0
e=m
for i in range(m):
    if len(choco) > 1:
        if choco[0] + choco[1] == choco[1] + choco[2]:
            sp = []
            for j in range(s, e):
                sp.append(choco[j])
            s = s + m - 1
            e += s
            sep_seg.append(sp)
        else:
            sp = []
            for j in range(s, e):
                sp.append(choco[j])
            s = s + m
            e += s
            sep_seg.append(sp)
    else:
        sp = []
        for j in range(s, e):
            sp.append(choco[j])
        s = s + m
        e += s
        sep_seg.append(sp)


count = 0
for k in sep_seg:
    r=0
    for x in k:
        r+=x
    if r == d:
        count+=1
if count > 0:
    print(count)
else:
    print(0)
print(sep_seg)



