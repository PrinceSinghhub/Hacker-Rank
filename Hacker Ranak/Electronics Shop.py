b,n,m = map(int,input().split())
keybord = list(map(int,input().split()))
usb= list(map(int,input().split()))

price = []
for i in keybord:
    if i<=b:
        for j in usb:
            if j<=b:
                r=i+j
                if r<=b:
                    price.append(r)
if len(price) == 0:
    print(-1)
else:
    price = max(price)
    print(price)