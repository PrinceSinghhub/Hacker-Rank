n=int(input())
data = list(map(int,input().split()))
data = sorted(data)

for i in range(len(data)):
    if i != len(data)-1:
        if data[i]!=data[i-1] and data[i]!=data[i+1]:
            print(data[i])
            break
    else:
        print(data[i])