# def mutate_string(string, position, character):
#     s = string;p=position;c=character
#     r=s[:p] + c + s[p+1:]
#     return r
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# todo second method
def mutate_string(string, position, character):
    s = string;p=position;c=character
    s1=list(s)
    s1[p] = c
    s=''.join(s1)
    return s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)