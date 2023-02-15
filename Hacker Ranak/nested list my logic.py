a =[]
n = int(input())
for i in range(n):
    b =[]
    name = input()
    grade = float(input())
    b.append(name)
    b.append(grade)
    a.append(b)
grade = []
for i in a:
    grade.append(i[1])
grade.sort()
second=grade[1]
name = []
while True:
    for i in a:
        if i[1] == second:
            name.append(i[0])


    break
name.sort()
for l in name:
    print(l)





