import random
import os
import time


def generate_number():
    return random.randint(1, 90)

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end='\t\t')
        print()

numbers = []
while len(numbers) < 8:
    num = generate_number()
    if num not in numbers:
        numbers.append(num)

numbers.sort()


bingo_board = [
    [numbers[0], numbers[1], numbers[2]],
    [numbers[3], numbers[4], 'BG!😛😝'],
    [numbers[5], numbers[6], numbers[7]]
]


while True:
    os.system('cls') 
    print_board(bingo_board)  

    try:
        user_input = int(input('\nENTER NUMBER🥰: '))
    except ValueError:
        print("Please enter a valid number.")
        time.sleep(2)
        continue

    
    for i in range(3):
        for j in range(3):
            if bingo_board[i][j] == user_input:
                bingo_board[i][j] = '❌'

    
    mark_count = 0
    for i in range(3):
        for j in range(3):
            if bingo_board[i][j] == '❌':
                mark_count += 1

    if mark_count == 8:
        os.system('cls')
        print_board(bingo_board)
        print("\n🎉 Congratulations! You’ve cleared the board! 🎉")
        break

    time.sleep(1)
