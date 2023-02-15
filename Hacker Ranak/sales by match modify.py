n=int(input())
arr = list(map(int,input().split()))
con_arr = list(set(arr))

result =0
for i in con_arr:
    d=0
    d+=arr.count(i)
    if d>1:
        if d % 2 == 0:
            t=d/2
            result += t
        elif d % 2 != 0:
            d = d - 1
            if d % 2 == 0:
                t = d / 2
                result += t
print(int(result))

