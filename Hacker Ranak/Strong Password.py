L = int(input())
passw = input()
dig = ''
upper = ''
lower = ''
special = ''

for i in passw:
    if i.isupper():
        upper+=i
    elif i.islower():
        lower+=i
    elif i.isdigit():
        dig+=i
    else:
        special+=i
    # print(dig,upper,lower,special)

if len(dig) == 0 or len(upper) == 0 or len(lower) == 0 or len(special) == 0:
    res = 0
    if len(dig) == 0:
        res += 1

    if len(upper) == 0:
        res += 1
    if len(lower) == 0:
        res += 1
    if len(special) == 0:
        res += 1

    if len(passw)>=6:
        print(res)
    else:
        if len(passw)<6 and res<4:
            print(res)


# if len(passw) > 6000:
#     res = 6 - len(passw)
#     print(res)
# else:
#     dig = ''
#     upper = ''
#     lower = ''
#     special = ''
#
#     for i in passw:
#         if i.isupper():
#             upper+=i
#         elif i.islower():
#             lower+=i
#         elif i.isdigit():
#             dig+=i
#         else:
#             special+=i
#     # print(dig,upper,lower,special)
#
#     if len(dig) == 0 or len(upper) == 0 or len(lower) == 0 or len(special) == 0:
#         res = 0
#         if len(dig) == 0:
#             res += 1
#
#         if len(upper) == 0:
#             res += 1
#         if len(lower) == 0:
#             res += 1
#         if len(special) == 0:
#             res += 1
#
#         print(res)
