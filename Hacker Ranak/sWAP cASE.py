def swap_case(s):
    String = s
    result=''
    for i in String:


        if i.islower():
            result=result+i.upper()

        elif i.isupper():
                result=result+i.lower()
        else:
            result+=i
    return result
if __name__ == '__main__':
    s = input("Enter string")
    result = swap_case(s)
    print(result)