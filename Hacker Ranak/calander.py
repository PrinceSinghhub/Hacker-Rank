import calendar
m,d,y=map(int,input().strip().split())
r=calendar.day_name[calendar.weekday(y,m,d)]
t=r.upper()
print(t)