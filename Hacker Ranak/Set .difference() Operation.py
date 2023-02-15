a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))
r=b.difference(d)
r1=0
for i in r:
    r1+=1
print(r1)