board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]

def main(board):             
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
