a = input()
b = []
for i in a:
    if i.isalnum():
        b.append(True)
    else:
        b.append(False)
c = any(b)
if c==True:
    print(True)

else:
    print(False)
#
b1 = []
for i in a:
    if i.isalpha():
        b1.append(True)
    else:
        b1.append(False)
c = set(b1)
if True in c:
    print(True)

else:
    print(False)

b3 = []
for i in a:
    if i.isdigit():
        b3.append(True)
    else:
        b3.append(False)
c = set(b3)
if True in c:
    print(True)

else:
    print(False)

b4 = []
for i in a:
    if i.islower():
        b4.append(True)
    else:
        b4.append(False)
c = set(b4)
if True in c:
    print(True)

else:
    print(False)

b5 = []
for i in a:
    if i.isupper():
        b5.append(True)
    else:
        b5.append(False)
c = set(b5)

if True in c:
    print(True)

else:
    print(False)

# todo 2 method
string = input()
l=list(string)
a,b,c,d,e=False,False,False,False,False
for i in l:
    if i.isalnum():
        a=True
    if i.isalpha():
        b=True
    if i.isdigit():
        c=True
    if i.islower():
        d=True
    if i.isupper():
        e=True
print(a)
print(b)
print(c)
print(d)
print(e)
s="codec"
print(any(s.isdigit() for i in s))