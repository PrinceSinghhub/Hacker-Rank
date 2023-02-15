q = int(input())
result = []
for i in range(q):
    data = list(map(int, input().split()))
    mouse=data[2]
    coutA = 0
    coutB =0
    Bcata = data[0];Scata = data[0]
    Bcatb = data[1];Scatb = data[1]

    if Bcata>mouse:
        while(Bcata>mouse):
            coutA+=1
            Bcata-=1
        result.append(coutA)

    if Scata < mouse:
        while (mouse>Scata):
            coutA += 1
            Scata += 1
        result.append(coutA)

    if Bcatb>mouse:
        while(Bcatb>mouse):
            coutB+=1
            Bcatb-=1
        result.append(coutB)

    if Scatb < mouse:
        while (mouse>Scatb):
            coutB += 1
            Scatb += 1
        result.append(coutB)


if len(result) == 2:
    if result[0] < result[1]:
        print("Cat A")
    elif result[0] > result[1]:
        print("Cat B")
    else:
        print("Mouse C")



else:
    subarr = []
    p = 2
    m = 0
    for i in range(len(result)):
        i += m
        subarr.append(result[i:p + i])
        m += 1

    for i in subarr:
        if len(i) > 1:
            if i[0] < i[1]:
                print("Cat A")
            elif i[0] > i[1]:
                print("Cat B")
            else:
                print("Mouse C")






