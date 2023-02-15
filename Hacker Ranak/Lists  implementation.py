List = []
N = int(input())
for i in range(N):
    x=input().split()
    if x[0]=="insert":
        a = int(x[1])
        b = int(x[2])

        List.insert(a, b)


    elif x[0]=="remove":
        a = int(x[1])

        List.remove(a)

    elif x[0]=="append":
        n1 = int(x[1])
        List.append(n1)

    elif x[0]== "sort":
        List.sort()

    elif x[0]=="pop":
        List.pop()

    elif x[0]=="reverse":
        List.reverse()

    elif x[0]=="print":
        print(List)

