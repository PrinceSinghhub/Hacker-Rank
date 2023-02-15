a=[-50,-50,50,50]

b = set(a)

b = list(b)

b.sort()

for i in a:
    print(i)
    if (i==b[1]):
        print(i)