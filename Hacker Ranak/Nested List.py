a =[]
n = int(input("Enter: "))
for i in range(n):
    b =[]
    name = input("Enter name: ")
    grade = float(input("ENter grade: "))
    b.append(name)
    b.append(grade)
    a.append(b)
grade = []
for i in a:
    grade.append(i[1])

grade = set(grade)
grade = list(grade)
grade.sort()
second = grade[1]
name = []
while True:
    for i in a:
        if second == i[1]:
                name.append(i[0])
    break
name.sort()
for l in name:
    print(l)
print(name)
print(grade)
