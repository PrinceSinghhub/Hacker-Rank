# todo 1st method
r=int(input())
t=input()
s=t.split()
for i in range(len(s)):
    s[i]  = int(s[i])
print(tuple(s))

# todo 2nd method
n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))

# vowels = ('a', 'e', 'i', 'o', 'u')
# print('The hash is:', hash(vowels))
