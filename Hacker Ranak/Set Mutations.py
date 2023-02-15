# n=int(input())
# Set = set(map(int,input().split()))
# a={2,3,5,6,8,9,1,4,7,11}
# Set.intersection_update(a)
# b={55,66}
# Set.update(b)
# c={22,7,35,62,58}
# Set.symmetric_difference_update(c)
# d={11,22,35,55,58,62,66}
# Set.difference_update(d)
# r=0
# for i in Set:
#     r+=i
# print(r)
#
n=int(input())
Set = set(map(int,input().split()))
cmd = int(input())
for i in range(cmd):
    command=input().split()
    if command[0] == "update":
        b=set(map(int,input().split()))
        Set.update(b)

    elif command[0] == "intersection_update":
        b = set(map(int, input().split()))
        Set.intersection_update(b)

    elif command[0]== "symmetric_difference_update":
        b = set(map(int, input().split()))
        Set.symmetric_difference_update(b)

    elif command[0] == "difference_update":
        b = set(map(int, input().split()))
        Set.difference_update(b)

result = 0
for i in Set:
    result+=i
print(result)
