import datetime
d = datetime.datetime.today().strftime('%Y-%m-%d').split('-')
for i in d:
    print(i)
