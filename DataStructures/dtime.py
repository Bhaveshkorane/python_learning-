import datetime

time=datetime.datetime.now()

print(time)
print("year:",time.year)
print("date:",time.date())
print("day:",time.day)
print("dst:",time.dst())
print("new format:",time.ctime())