import datetime
today = datetime.date.today()
print (today)
holiday = datetime.date(year=2022, month=10, day=15)
if holiday > today:
    print('coming soon')
elif holiday< today:
    print('hope you enjoyrd it')
else: 
    print('holiday time')