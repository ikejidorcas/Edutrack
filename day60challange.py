import datetime
while True:
    original = datetime.date.today()
    year = int(input('Enter year of event: '))
    day = int(input('enter day of event: '))
    month = int(input('enter month of event: '))
    yo = datetime.date(year,day,month)
    omo = yo - original
    omo = omo.days
    q1= print(omo)
    if  omo >0:
        print('Am sorry the event don pass 😥')
        print(f'the date was actually {original} so yoy are {q1} behind')
    elif omo<0:
        print('okay the event never reach🥰')
        print(f'the date is actually {original} so it is in {q1} time')
    else:
    
        print('you are right on time come in')
