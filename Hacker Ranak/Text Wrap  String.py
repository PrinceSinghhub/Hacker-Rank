import textwrap
def wrap(string, max_width):
    f=textwrap.wrap(string,max_width)
    r = ''
    for i in f:
        r+=i
        r+='\n'
    return r

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)