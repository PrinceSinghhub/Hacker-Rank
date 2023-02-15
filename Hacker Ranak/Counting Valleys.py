def Valley_Count(step,comm):
    level = 0
    ans = 0
    for i in comm:
        if i == "D":
            level-=1
        elif i == "U":
            level+=1
            if level == 0:
                ans+=1

    return ans

s=8
c="UDDDUDUU"
print(Valley_Count(s,c))