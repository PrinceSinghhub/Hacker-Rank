y = int(input().strip())
count=0
if(y>1918 and y<=2700):
    if(y%400==0 or (y%4==0 and y%100!=0)):
        count=1
    if(count==1):
        print('12.09.'+str(y))
    else:
        print('13.09.'+str(y))
if(y<1918 and y>=1700):
    if(y%4==0):
        count=1
    if(count==1):
        print('12.09.'+str(y))
    else:
        print('13.09.'+str(y))
if(y==1918):
    print('26.09.1918')