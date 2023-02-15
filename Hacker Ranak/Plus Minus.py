n=int(input())
arr=list(map(int,input().split()))
pos=0
neg=0
eql =0
for i in arr:
    if i>0:
        pos+=1
    if i<0:
        neg+=1
    if i==0:
        eql+=1
# todo concept of String formating
print('{:.6f}'.format(pos/n))
print('{:.6f}'.format(neg/n))
print('{:.6f}'.format(eql/n))