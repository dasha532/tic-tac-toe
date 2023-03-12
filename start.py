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
start_game()