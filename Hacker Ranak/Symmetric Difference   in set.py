a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))

r=b.symmetric_difference(d)
r=sorted(r)
for i in r:
    print(i)

# r=[]
# r1 = len(b)
# r2 = len(d)
# if r1>r2:
#     for i in range(r2,r1):
#         a=b[0]
#         d.append(a)
# elif r2>r1:
#     for i in range(r1,r2):
#         a = b[0]
#         b.append(a)
# t=len(b)
# for i in range(t):
#     if b[i] == d[i]:
#         continue
#     elif b[i]!=d[i]:
#         r.append(b[i])
#         r.append(d[i])
#
# r=sorted(r)
# r=tuple(r)
# print(b)
# print(d)
# for i in r:
#     print(i)

