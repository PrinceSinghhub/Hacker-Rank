n=int(input())
l=[]
for i in range(1,n+1):
    x=input()
    l.append(x)
l=set(l)
print(len(l))