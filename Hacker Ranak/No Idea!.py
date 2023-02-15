n,m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = 0

for i in arr:
    if i in A:
        result+=1

    elif i in B:
        result-=1

print(result)
