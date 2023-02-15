x1,v1,x2,v2 = map(int,input().split())
exist = False
while True:
    if x1 == x2:
        exist = True
        break
    if (v1 > v2 and x1 > x2) or (v2 > v1 and x2 > x1) or (v2 == v1 and x2 != x1):
        break
    x1 += v1
    x2 += v2

if exist == True:
    print('YES')
else:
    print('NO')