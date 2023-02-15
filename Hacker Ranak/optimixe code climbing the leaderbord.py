def find_rank(rank,player):

    rank = sorted(list(set(rank)))[::-1]
    player = sorted(player)[::-1]
    res = []

    j = 0
    l =len(rank)

    for i in range(len(player)):
        while j<l and player[i]<rank[j]:
            j+=1
        res.append(j+1)
    return res[::-1]
r = list(map(int,input().split()))
p = list(map(int,input().split()))
ans = find_rank(r,p)
for i in ans:
    print(i)
