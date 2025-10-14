vowels = ['A', 'E', 'I', 'O', 'U']
q1 = input('Enter Sentence🥰: ')
print(q1)
for w in q1:
    if w.upper() in vowels:
        print('\033[94m', end ='')
    print(w, end='')
    print('\033[0m', end ='')