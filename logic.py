# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] or \
           board[0][i] == board[1][i] == board[2][i]:
            return board[i][i]

    # Check the two diagonal lines
    if board[0][0] == board[1][1] == board[2][2] or \
       board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    
    return None


def other_player(current_user):
    if current_user == "X":
        return "O"
    elif current_user == "O":
        return "X"
    else:
        return None