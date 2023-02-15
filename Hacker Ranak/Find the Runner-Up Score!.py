n = int(input())
List = list(set(map(int,input().split())))
List.sort()
print(List[-2])
