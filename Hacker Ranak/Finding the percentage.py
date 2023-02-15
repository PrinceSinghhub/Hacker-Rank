# n = int(input("Enter no of Student: "))
# student_marks = {}
# for i in range(n):
#     name, *line = input("Name and marks: ").split(" ")
#     scores = list(map(float, line))
#     student_marks[name] = scores
#     print(student_marks)
# # query_name = input("Check name: ")
# # output = list(student_marks[query_name])
# # per = sum(output)/len(output)
# # print("%.2f" % per)

def pr():
    n = int(input("Enter range: "))
    a = {}
    result = 0
    for j in range(n):
        name,*data = input("Check name: ").split()
        f = []
        for i in data:
            i = int(i)
            f.append(float(i))
        a[name] = f

    query_name = input("Search Name: ")
    for key,value in a.items():
        if query_name == key:
            result = a[key]
    Sum = sum(result)
    average = Sum/3
    print('%.2f' %average)
pr()

