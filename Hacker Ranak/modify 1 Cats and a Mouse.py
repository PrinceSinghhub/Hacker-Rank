q = int(input())
result = []
for i in range(q):
    data = list(map(int, input().split()))
    x = abs(data[0] - data[2])
    y = abs(data[1] - data[2])
    if x>y:
        result.append('Cat B')
    elif x<y:
        result.append('Cat A')
    else:
        result.append('Mouse C')

for j in result:
    print(j)