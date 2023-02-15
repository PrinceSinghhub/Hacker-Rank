a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))
r=b.intersection(d)
khushi=0
for i in r:
    khushi+=1
print(khushi)