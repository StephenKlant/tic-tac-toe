""" 
Игра "Крестики-нолики" by Степан
"""


# Создать игровую доску
board = [i for i in range(9)]


for i in range(len(board)):   
    board[i] = i + 1

print(board)

def show_board():
    """Отображение игрового поля"""
    print('\n' + '----' + 'Игровое поле' + '----', end='')
    n = 0; h = 3
    board_display = []
    for j in range(3):
        variable = []
        for i in board[n:h]:
            variable.append(i)
        board_display.append(variable)
        n += 3; h += 3  
    print('\n')
    for i in board_display:
        for j in i: 
            print(j, end=' ')
        print('\n')

def game_step():
    """Ход игрока"""

    players = ['Игрок 1(X)', 'Игрок 2(O)']
    # valid = True
    n = 0
    while n < len(board)//2 :
        for player in players:
            chioce = int(input(f"Ходите, {player} (Введите число от 1 до 9):  ")) - 1
            if player == 'Игрок 1(X)':
                board[chioce] = 'X'
            else: board[chioce] = 'O'
            show_board()
        n += 1
        # valid = False
    chioce = int(input("Ходите, Игрок 1(X) (Введите число от 1 до 9):  ")) - 1
    board[chioce] = 'X'
    show_board()

def check_win():
    """Проверка победы"""
    
    

    win_coord = ((0, 3, 6), (1, 4, 7), (2, 5, 8), 
                 (0, 1, 2), (3, 4, 5), (6, 7, 8), 
                 (0, 4, 8), (2, 4, 6))
    
    for tuplee in win_coord:
        if board[tuplee[0]] == 'O' and board[tuplee[1]] == 'O' and board[tuplee[2]] == 'O': return 'Победил Игрок 2'
        elif board[tuplee[0]] == 'X' and board[tuplee[1]] == 'X' and board[tuplee[2]] == 'X': return 'Победил Игрок 1'
    return 'Ничья'    

def loop():
    """Цикл Игры"""

    show_board()
    game_step()
    print(check_win())

loop()