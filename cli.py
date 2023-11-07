# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player, is_board_full


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_user = 'O'
    while winner is None:
        print(f"Player {current_user}: take a turn!")

        # TODO: Show the board to the user.
        for row in board:
            print(row)

        # TODO: Input a move from the player.
        while True:
            try:
                move = input(f'Player {current_user},please enter your next move, ranging from 0 to 2 (format: x,y): ')
                x, y = map(int, move.split(','))
                if board[x][y] is None:
                    break
                else:
                    print("This position is already taken. Try another one.")
            except(IndexError, ValueError):
                print('Invalid input, please follow the rule.')

        # TODO: Update the board.
        board[x][y] = current_user

        # TODO: Update who's turn it is.
        current_user = other_player(current_user)
        winner = get_winner(board)
        if winner is None and is_board_full(board):
            print("It's a draw!")
            break 
    if winner:
      print(f'player{winner} wins!')