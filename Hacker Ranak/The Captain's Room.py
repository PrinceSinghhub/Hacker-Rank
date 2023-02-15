n=int(input())
data = list(map(int,input().split()))
Set = set(data)
List = list(Set)

for j in range(len(List)):
    re = 0
    for i in range(len(data)):
        if List[j] == data[i]:
            re+=1
    if re == 1:
        print(List[j])


