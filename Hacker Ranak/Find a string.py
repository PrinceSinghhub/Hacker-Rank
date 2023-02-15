def count_substring(string, sub_string):
    result = 0
    s=string
    su=sub_string
    L=len(s)
    Ls = len(su)
    for i in range(L - Ls + 1):
        if (s[i:i + Ls] == sub_string):
            result += 1
    return result


# if __name__ == '__main__':
def findstring():
    string = input('Enter First String: ').strip()
    sub_string = input('Enter Second String: ').strip()

    count = count_substring(string, sub_string)
    print(f"No of Present SubString is: {count}")
findstring()
