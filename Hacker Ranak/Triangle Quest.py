a=int(input())
for i in range(1,a):
    for j in range(0,i):
        print(i,end="")
    print()
# todo second method
for i in range(1,int(input())):
    print(int(i*(pow(10,i)/9)))

