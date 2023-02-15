List = []
N = int(input("Enter command line: "))
for i in range(N):
    x=input("Enter Command: ")
    if x=="insert":
        print("indesx and element")
        n=int(input("Enter index: "))
        n1=int(input("Enter element: "))
        List.insert(n,n1)
    elif x=="print":
        print(List)
    elif x=="remove":
        n1 = int(input("Enter element: "))
        List.remove(n1)
    elif x=="append":
        n1 = int(input("Enter element: "))
        List.append(n1)
    elif x == "sort":
        List.sort()

    elif x=="pop":
        List.pop()

    elif x=="reverse":
        List.reverse()