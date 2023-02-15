a=int(input())
count = [0]*a
arr = list(map(int,input().split()))
for t in arr:
    count[t] = count[t]+1
print(count)
print(count.index(max(count)))
