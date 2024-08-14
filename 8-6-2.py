import datetime
t_delta = datetime.timedelta(days=1)
dt = datetime.datetime.strptime("2024/08/13 15:45", "%d/%m/%y %H:%M")
print(dt + t_delta)
