# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import TicTacToe

# Reminder to check all the tests

if __name__ == '__main__':
    game = TicTacToe()

    num_players = int(input("Enter the number of players (1 or 2): "))

    if num_players == 1:
        game.play_single_player()
    elif num_players == 2:
        game.play_two_players()
    else:
        print("Invalid number of players. Please choose 1 or 2.")