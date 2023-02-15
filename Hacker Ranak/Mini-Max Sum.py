data = list(map(int,input().split()))
r=[]

for i in range(len(data)):
    el = 0
    for j in range(i+1,len(data)):
        el+=data[j]
    for k in range(i-1,-1,-1):
        el+=data[k]
    r.append(el)
r.sort()
print(r[0],r[len(r)-1])