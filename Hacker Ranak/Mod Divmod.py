def pr(a,b):
    x=a//b
    y=a%b
    z=divmod(a,b)
    print(f"{x}\n{y}\n{z}")
a=int(input("Enter No1: "))
b=int(input("Enter No2: "))
pr(a,b)