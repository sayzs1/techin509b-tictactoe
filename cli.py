# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import random

class TicTacToe:
    def __init__(self):
        self.board = self.make_empty_board()
        self.current_user = 'O'
        self.winner = None

    @staticmethod
    def make_empty_board():
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def display_board(self):
        for row in self.board:
            print(row)

    def input_move(self):
        while True:
            try:
                move = input(f'Player {self.current_user}, please enter your next move, ranging from 0 to 2 (format: x,y): ')
                x, y = map(int, move.split(','))
                if self.is_valid_move(x, y):
                    break
                else:
                    print("Invalid move. Try another one.")
            except (IndexError, ValueError):
                print('Invalid input, please follow the rule.')

        return x, y

    def is_valid_move(self, x, y):
        return 0 <= x <= 2 and 0 <= y <= 2 and self.board[x][y] is None

    def update_board(self, x, y):
        self.board[x][y] = self.current_user

    def switch_player(self):
        self.current_user = self.other_player()

    def other_player(self):
        if self.current_user == "X":
            return "O"
        elif self.current_user == "O":
            return "X"
        else:
            return None

    def get_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] or \
               self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[i][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] or \
           self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[1][1]

        return None

    def is_board_full(self):
        for row in self.board:
            if None in row:
                return False
        return True

    def play_single_player(self):
        while self.winner is None and not self.is_board_full():
            self.display_board()

            if self.current_user == 'O':
                x, y = self.input_move()
            else:
                x, y = random.randint(0, 2), random.randint(0, 2)
                while not self.is_valid_move(x, y):
                    x, y = random.randint(0, 2), random.randint(0, 2)

            self.update_board(x, y)
            self.switch_player()
            self.winner = self.get_winner()

        self.display_result()

    def play_two_players(self):
        while self.winner is None and not self.is_board_full():
            self.display_board()
            x, y = self.input_move()
            self.update_board(x, y)
            self.switch_player()
            self.winner = self.get_winner()

        self.display_result()

    def display_result(self):
        self.display_board()
        if self.winner:
            print(f'Player {self.winner} wins!')
        else:
            print("It's a draw.")
