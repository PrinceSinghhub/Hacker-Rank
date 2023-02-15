def angryProfessor(k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1

    if count >= k:
        return "NO"
    return "YES"