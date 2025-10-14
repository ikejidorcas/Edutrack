contestant = []
def prettyprint():
    for row in contestant:
        for item in row:
            print(f'{ item:^10}',end= ' | ' )
            
        print()
       
while True:
    q1 = input('add or remove? ')
    if q1.strip().lower()[0]== 'a':
        name = input('ENTER NAME🥰: ')
        age = input('ENTER AGE🙂: ')
        talent = input('ENTER TALENT😮: ')
        row = [name, age, talent]
        contestant.append(row)
    else:
        q2 = input('what is the name of the record to delete: ')
        for row in contestant:
            if q2 in row:
                contestant.remove(row)
    prettyprint()


