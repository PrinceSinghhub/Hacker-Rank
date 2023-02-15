def findDigits(n):
    org = n
    count = 0

    while n > 0:

        digit = n % 10
        if digit != 0 and org % digit == 0:
            count += 1
        n = n // 10

    return count

print(findDigits(124))