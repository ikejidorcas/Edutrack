def col(q1):
    if q1 == 'r':
        print('\033[31m', end='')
    elif q1 == 'b':
        print('\033[94m', end='')
    elif q1 == 'g':
        print('\033[32m', end='')
    elif q1 == 'p':
        print('\033[35m', end='')
q2 = input('LET"S DO SOMETHING CRAZY😛😛 \n Enter sentence😏😛💖:')
print(q2)
for t in q2:
    col(t.lower())
    print(t, end='')
