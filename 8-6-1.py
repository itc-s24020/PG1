from datetime import datetime
now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

dum_day  = datetime(2019, 5, 1, hour=15, minute=15, second=15)
print(dum_day)
t_str ='202408131541'
dt = datetime.strptime(t_str, "%Y%m%d%H%M%S")
print(dt)
dt2 = dt.strftime("%Y年%m月%d日 %H時%m分")
print(dt2)
