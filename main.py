import random
def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', end=' ')
        for g in range(3):
            print(board[i][g], end=' | ')
        print('\n-------------')
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    for g in range(3):
        if board[0][g] == board[1][g] == board[2][g] != " ":
            return board[0][g]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    if all(board[i][g] != " " for i in range(3) for g in range(3)):
        return 'Draw'
    return None
def player(board):
    while True:
        row = int(input('Введіть номер строки (0-2): '))
        col = int(input('Введіть номер столбца (0-2): '))
        if board[row][col] == ' ':
            board[row][col] = 'X'
            break
        else:
            print('Невірний хід. Спробуйте ще раз.')

def computer(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_winner(board, 'O'):
                    return
                else:
                    board[row][col] = ' '

while True:
    x = random.randint(0, 2)
    y = random.randint(0, 2)