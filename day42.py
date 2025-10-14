players_info = {'BEAST NAME😛 ': None, 'BEAST TYPE😛🤩': None, 'SPECIAL MOVE 😏🤍': None, 'STARTING HP🥰💜': None, 'STARTING MP': None}

for q1, q2 in players_info.items():
    players_info[q1] = input(f'{q1}: ').strip().title().capitalize()

if players_info['BEAST TYPE😛🤩'] == 'Air beast':
    print(f'\033[32m ', end= '\t')
if players_info['BEAST TYPE😛🤩']== 'Water beast':
    print(f'\033[94m', end='\t' )
if players_info['BEAST TYPE😛🤩'] == 'Fire beast':
    print(f'\033[31m ', end= '\t')

for q1, q2 in players_info.items():
    print(f'{q1 }: {q2}')
   
