d=int(input())
marks = []
grade = []

for i in range(d):
    n=int(input())
    marks.append(n)


for j in range(len(marks)):
    e = marks[j]
    while True:

        if e%5!=0:
            e+=1

        if e%5 == 0:
            grade.append(e)

            break
result = []
L = len(marks)
for i in range(L):
    for j in range(i,i+1):
        c = grade[i] - marks[j]
        if c < 3 and marks[i]>37:

            result.append(grade[i])
        elif c >= 3 and marks[i]>37:
            result.append(marks[j])
        else:
            result.append(marks[i])
for j in result:
    print(j)


