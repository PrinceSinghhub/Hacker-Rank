rc = int(input())
r=[]
for i in range(rc):
    l = list(map(int,input().split()))
    r.append(l)
left = 0
for i in range(rc):
    left+=(r[i][i])
t=0
d=rc-1
right=0

while(d>=0):
    right+=(r[t][d])
    t+=1
    d-=1
result = left-right
print(abs(result))