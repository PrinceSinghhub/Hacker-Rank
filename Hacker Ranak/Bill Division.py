n,k = map(int,input().split())
price = list(map(int,input().split()))
b = int(input())
price.remove(price[k])
Sum = sum(price)
mon = Sum/2
give = b - mon
if b == mon:
    print("Bon Appetit")
    quit()
print(int(give))