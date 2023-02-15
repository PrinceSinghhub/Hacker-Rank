n = int(input())
choco = list(map(int,input().split()))
d,m = map(int,input().split())

num_ways = 0
for i in range(len(choco)-m+1):
    if sum(choco[i:i+m]) == d:
        num_ways += 1


print(num_ways)