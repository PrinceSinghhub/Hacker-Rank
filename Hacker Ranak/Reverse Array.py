def reverse(arr):
    result = []
    for i in range(len(arr)-1,-1,-1):
        result.append(arr[i])
    for j in result:
        print(j,end=" ")
n = int(input())
arry = list(map(int,input().split()))
reverse(arry)