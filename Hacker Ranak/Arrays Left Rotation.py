def rotLeft(a, d):
    rotate = a[0:d]
    remain = a[d::]

    return remain + rotate
