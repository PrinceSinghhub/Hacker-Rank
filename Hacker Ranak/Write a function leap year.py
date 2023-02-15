def khushi(year):
    Year = year
    if Year%4==0 and Year%100!=0 or Year%400==0:
        return True
    else:
        return False
x=int(input())
print(khushi(x))
