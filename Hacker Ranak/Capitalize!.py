def pr():
    s = input()
    result = ''
    result+=s[0].upper()
    a=1
    b=len(s)
    while(a<b):

        if s[a]==' ':
            t=a+1
            result+=' '
            result += s[t].upper()
            a+=2

        else:
            result+=s[a]
            a+=1



    print(result)
    # print(type(String))
pr()
a="codex coder"
a=a.title()
print(a)