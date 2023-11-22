def get_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] or \
           board[0][i] == board[1][i] == board[2][i]:
            return board[i][i]

    if board[0][0] == board[1][1] == board[2][2] or \
       board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]

    return None