def beautifulDays(i, j, k):
    count = 0

    for i in range(i, j + 1):

        org = i
        rev = int(str(i)[::-1])

        remain = org - rev
        if remain % k == 0:
            count += 1

    return count

