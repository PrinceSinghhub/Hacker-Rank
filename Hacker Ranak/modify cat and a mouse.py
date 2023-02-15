output = []
def cast_and_mouse(cata,catb,mouse):
    X = abs(cata - mouse)
    Y = abs(catb- mouse)
    if X > Y:
        output.append('Cat B')
    elif X < Y:
        output.append('Cat A')
    else:
        output.append('Mouse C')

n = int(input())
for i in range(n):
    catA, catB, mouseC = map(int, input().split())
    cast_and_mouse(catA, catB, mouseC)

for i in output:
    print(i)
