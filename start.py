board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3


def print_board():  # Печать игрового поля
    for i in range(size):
        print('', board[i * 3], ' ', board[1 + i * 3], ' ', board[2 + i * 3])


def stepping(index, char):  # Ход игрока
    if index < 1 or index > 9 or board[index - 1] in ('X', 'O'):
        return False
    board[index - 1] = char
    return True


def win_ind():  # Проверка на победу
    win = False
    comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))
    for i in comb:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]]:
            win = board[0]
    return win


def AI(char):  # Алгоритм ИИ
    comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))
    for i in comb:
        if board[i[0]] == board[i[1]]:
            board[i[2]] = char
            return
        elif board[i[1]] == board[i[2]]:
            board[i[0]] = char
            return
        elif board[i[2]] == board[i[0]]:
            board[i[1]] = char
            return
    if board[4] != 'X' and board[4] != 'O':
        board[4] = char
    elif board[6] != 'X' and board[6] != 'O':
        board[6] = char
    elif board[2] != 'X' and board[2] != 'O':
        board[2] = char
    elif board[3] != 'X' and board[3] != 'O':
        board[3] = char
    else:
        board[8] = char


def start_gameAI():  # Игра с ИИ
    print("Игровое поле: ")
    step = 1
    print_board()
    player = 'X'
    print("Ваш ход первый:")
    while (0 < step < 10) and (win_ind() is False):
        if step % 2 != 0:
            index = input("Ход игрока " + player + " Введите номер поля куда хотите сделать ход:")
            if index == '0':
                break
            if stepping(int(index), player):
                print("Отличный ход")
                step += 1
                print_board()
            else:
                print("Повторите ход!")
        else:
            print("Ход компьютера:")
            if player == 'X':
                AI('O')
            else:
                AI('X')
            print_board()
            step += 1
    if win_ind():
        print("Выиграл " + str(win_ind()))
    else:
        print("Ничья")
    print("GAME OVER")


def start_game():  # Игра на двоих
    print("Игровое поле: ")
    player = "X"
    step = 1
    print_board()
    while (0 < step < 10) and (win_ind() is False):
        index = input("Ход игрока " + player + " Введите номер поля куда ходтите сделать ход:")
        if index == '0':
            break
        if stepping(int(index), player):
            print("Отличный ход")
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            print_board()
            step += 1
        else:
            print("Повторите ход!")
    if win_ind():
        print("Выиграл " + str(win_ind()))
    else:
        print("Ничья")
    print("GAME OVER")


print("Добро пожаловать в игру!")
a = int(input("Выберете режим игры: 1 - одиночная, 2 - игра на двоих"))
if a == 1:
    start_gameAI()
else:
    start_game()
