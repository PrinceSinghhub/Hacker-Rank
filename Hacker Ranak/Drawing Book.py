n = int(input())
p = int(input())
d = []
for p1 in range(1,n+1):
    d.append(p1)

l = len(d)
r = []

ran = []
for i in range(l+1):
    if i == 0:
        ran.append(i)
    if i%2!=0:
        ran.append(i)

e = 1
for j in ran:
    r.append(d[j:e])
    e+=2


for k in r:
    if len(k) == 0:
        r.remove(k)


# todo search
front = 0
end = 0


for i in r:
    for j in i:
        if j==p:
            c = r.index(i)
            front+=c
            break

re = []
for x in range(len(r)-1,-1,-1):
    re.append(r[x])

for i in re:
    for j in i:
        if j==p:
            c = re.index(i)
            end+=c
            break

if front<end:
    print(front)
elif end<front:
    print(end)
else:
    print(front)



# todo optimize code

n = int(input())
p = int(input())

r=(int(p/2))
r1=int(n/2)-int(p/2)
print(min(r,r1))