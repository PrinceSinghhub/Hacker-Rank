# todo my approch
# n = int(input())
# arr = list(map(int,input().split()))
# arr_collaction = []
# for i in range(len(arr)):
#     dub_arr = []
#     for j in range(i,len(arr)):
#         data = abs(arr[i]-arr[j])
#         if data == 0 or data == 1:
#             dub_arr.append(arr[j])
#     arr_collaction.append(dub_arr)
#
# max = 0
#
# for i in arr_collaction:
#     if len(i)>=max:
#         max=len(i)
# print(max)

def picknumber(arr):
    result = 0
    for i in range(len(arr)):
        maxCount = max(arr.count(arr[i]) + arr.count(arr[i] + 1), arr.count(arr[i]) + arr.count(arr[i] - 1))
        if maxCount > result:
            result = maxCount
    return result

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = picknumber(arr)
print(result)


