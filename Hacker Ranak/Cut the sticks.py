def cutTheSticks(arr):

    ans = []

    while len(arr)>0:
        count = 0

        Min = min(arr)
        for i in range(len(arr)):

            arr[i] = arr[i]-Min
            count+=1

        while 0 in arr:
            arr.remove(0)
        ans.append(count)
    return ans

L = int(input())
ans = list(map(int,input().split()))
print(cutTheSticks(ans))




