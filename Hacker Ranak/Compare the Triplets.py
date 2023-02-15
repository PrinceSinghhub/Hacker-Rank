a=list(map(int,input().split()))
b=list(map(int,input().split()))
Alice = 0
Bob = 0
for i in range(len(a)):
    if a[i] > b[i]:
        Alice+=1
    elif a[i]<b[i]:
        Bob+=1
print(Alice,Bob)
