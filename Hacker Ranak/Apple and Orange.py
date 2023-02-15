s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
appel = list(map(int,input().split()))
orange = list(map(int,input().split()))
appel_data =[]
orange_data = []
for i in appel:
    appel_data.append(a+i)

for j in orange:
    orange_data.append(b+j)
apple_count = 0
orange_count = 0
for i in range(len(appel_data)):
    if appel_data[i] >= s and appel_data[i] <=t:
        apple_count+=1
for j in range(len(orange_data)):
    if orange_data[j] >= s and orange_data[j] <=t:
        orange_count+=1
print(apple_count)
print(orange_count)