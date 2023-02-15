n=int(input())
arr =list(map(int,input().split()))
long = max(arr)
arr_long =[]
count = []
for i in range(1,long+1):
    c= 0
    for j in arr:
        if i==j:
            c+=1
    if c>1:
        arr_long.append(i)
        arr_long.append(c)
data_arr = []
for i,j in enumerate(arr_long):

    if i%2!=0:

        count.append(arr_long[i])
        data_arr.append(arr_long[i-1])

count1 = max(count)
result = []
for i in range(len(count)):
    if count[i] == count1:
        result.append(data_arr[i])


# print(data_arr)
# print(count)
d=len(result)-2
print(result[d])
