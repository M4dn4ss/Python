from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

present = datetime.now()
present = datetime.today()

result = datetime.now()
result = present.year
result = present.month
result = present.day
result = present.hour
result = present.minute
result = present.second
result = datetime.ctime(present)
result = datetime.strftime(present, '%Y')
result = datetime.strftime(present, '%X')
result = datetime.strftime(present, '%D')
result = datetime.strftime(present, '%A')
result = datetime.strftime(present, '%B')
result = datetime.strftime(present, '%Y %B %D')

t = "15 April 2019 hour 10:12:30"
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1983, 5, 9,12,30,10)

result = datetime.timestamp(birthday) # second
result = datetime.fromtimestamp(result) # from second to datetime
result = datetime.fromtimestamp(0)

result = present - birthday # timedelta

# result = result.days
# result = result.seconds
# result = result.microseconds
print(present)
# result = present + timedelta(days=10)
# result = present + timedelta(days=730, minutes = 10)

result = present - timedelta(days = 10)
print(result)