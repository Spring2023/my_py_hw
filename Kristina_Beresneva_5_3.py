#Author Kristina Beresneva
#28.02.2022
#task: создать игру крестики-нолики

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  #список для поля

checklist = [1, 2, 3, 4, 5, 6, 7, 8, 9]       #список для возможных ходов

compSign = "X"       #игрок-компьютер
userSign = "0"       #игрок

def display_board(board):          #нарисовать игровое поле
    print("+-------" * 3,"+", sep="")
    for row in range(3):
        print("|       " * 3,"|", sep="")
        for col in range(3):
                print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")
    print()   
display_board(board)

board[1][1] = "X"                #первый ход компьютера в центр поля
display_board(board)
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

def check_win(board):        #проверка победы
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        elif board[0][i] == board[1][i] == board[2][i]:
            return True
        elif board[0][0] == board[1][1] == board[2][2]:
            return True
        elif board[2][0] == board[1][1] == board[0][2]:
            return True
        else:    
            return False
    return False
check_win(board)

def main(board):             #сама игра
    counter = 1
    win = False
    while not win:
        display_board(board)
        if counter % 2 == 0:
            enter_move(board)
        else:
            comp_move(board)
        counter += 1
        if counter > 4:
            check_win(board)
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

