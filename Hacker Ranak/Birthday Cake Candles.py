n=int(input())
data = list(map(int,input().split()))
data.sort()
stor = data[n-1]
count = 0
for i in data:
    if i == stor:
        count+=1
print(count)


