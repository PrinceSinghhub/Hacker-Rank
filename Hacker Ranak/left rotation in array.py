n,d = map(int,input().split())
arr = list(map(int,input().split()))
print(arr)
for i in range(d):
    arr.append(arr[0])
    arr.pop(0)

for i in arr:
    print(i,end=" ")