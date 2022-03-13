board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]

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


