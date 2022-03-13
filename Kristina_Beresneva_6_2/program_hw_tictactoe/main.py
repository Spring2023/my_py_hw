board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  #список для поля

checklist = [1, 2, 3, 4, 5, 6, 7, 8, 9]       #список для возможных ходов

compSign = "X"       #игрок-компьютер
userSign = "0"       #игрок

from sys import path

path.append("..\\packages")

from packages.tictactoe import module_display_board #импортируем игровое поле

board[1][1] = "X"                #первый ход компьютера в центр поля
module_display_board.display_board(board)
checklist.remove(5)

def enter_move(board):           #ход игрока
    flag = True
    while flag:
        move = int(input("Enter your move from 1 to 9: "))
        if move not in checklist:
            print("Error. Not empty!")
            continue
        flag = False
        checklist.remove(move)
        board[(move - 1) // 3][(move - 1) % 3] = userSign
enter_move(board)

def comp_move(board):           #ход компьютера
    move = checklist[0]
    checklist.remove(move)
    board[(move - 1) // 3][(move - 1) % 3] = compSign
comp_move(board)

from packages.tictactoe import module_check_win   #проверка победы
module_check_win.check_win(board)

def main(board):             #сама игра
    counter = 1
    win = False
    while not win:
        module_display_board.display_board(board)
        if counter % 2 == 0:
            enter_move(board)
        else:
            comp_move(board)
        counter += 1
        if counter > 4:
            module_check_win.check_win(board)
            if True:
                if counter % 2 == 0:
                    print("Выиграл 0!")
                    break
                else:
                    print("Выиграл X!")
                    break
        if counter == 9:
            print("Ничья!")
            break
main(board)
