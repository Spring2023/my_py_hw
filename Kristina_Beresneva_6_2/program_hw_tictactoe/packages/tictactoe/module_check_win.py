board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]

def check_win(board):        
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
