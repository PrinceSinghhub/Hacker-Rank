n=int(input())
string = []
for i in range(n):
    str = input()
    string.append(str)

q = int(input())
queries = []
for j in range(q):
    str = input()
    queries.append(str)

# todo check
for i in queries:
    result = 0
    for j in string:
        if j == i:
            result+=1
    print(result)
