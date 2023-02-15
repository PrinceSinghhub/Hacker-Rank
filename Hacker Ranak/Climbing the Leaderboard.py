def find_rank(rank,player):

    position = 0
    rev = []
    for i in range(len(rank)-1,-1,-1):
        rev.append(rank[i])
    for i in range(len(rev)):
        if rev[i] == player:
            position = i+1
            rev.clear()
            break
    return position


def rank_deside(rank,player,rl,pl):

    ans = []

    for i in player:

        rank = list(set(rank))
        rank.append(i)
        rank.sort()

        P = find_rank(rank,i)
        ans.append(P)

    for i in ans:
        print(i)

rl = int(input())
rank = list(map(int,input().split()))
pl = int(input())
player = list(map(int,input().split()))
rank_deside(rank,player,rl,pl)
