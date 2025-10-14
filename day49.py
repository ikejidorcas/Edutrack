"""e = open('biancafile.tst', 'r')
while True:
    w = e.readline().strip()
    if w =='':
        break
    print(w)
e.close()"""



q = open('didi. list', 'r')

q1 = q.read().split('\n')

q.close()   

score = 0
name = None

for rows in q1:
    q3 = rows.split()
    if q3 != []:
        if int(q3[1]) > score:
            score = int(q3[1])
            name = q3[0]
            print('THE WINNER IS ', name, 'WITH', score )


  