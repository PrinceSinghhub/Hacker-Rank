def convert(a):
    T = ''
    if a[-2:] == "AM":
        if (a[:2]) == "12":
            T=T+str("00"+a[2:8])
        else:
            T+=a[:-2]

    if a[-2:] == "PM":
        if a[:2] == "12":
            T+=a[:-2]

        else:
            T+=str(int(a[:2])+12) + a[2:8]

    return T


a = input()
d=convert(a)
print(d)
