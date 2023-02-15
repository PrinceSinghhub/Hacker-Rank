n,k = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
res = []
for e,j in enumerate(arr):
    f=[]
    for i in range(e+1,len(arr)):
        # if j < arr[i]:
        r = arr[i] + j
        if r % k == 0:
            f.append(j)
            f.append(arr[i])
            count += 1
    if len(f) > 0:
        res.append(f)
print(count)
print(res)
# count = 0
#
# for i, e in enumerate(arr):
#     for j in range(i + 1, len(arr)):
#         if e<arr[j]:
#             if (e + arr[j]) % k == 0:
#                 count += 1
#
# print(count)