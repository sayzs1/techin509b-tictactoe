# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import random
import logging

class Human:
    def __init__(self, name):
        self.name = name

    def make_move(self):
        move = input(f'{self.name}, please enter your next move, ranging from 0 to 2 (format: x,y): ')
        x, y = map(int, move.split(','))
        return x, y

class Bot:
    def __init__(self, name):
        self.name = name

    def make_move(self):
        x, y = random.randint(0, 2), random.randint(0, 2)
        return x, y

class TicTacToe:
    def __init__(self, player1, player2):
        self.board = self.make_empty_board()
        self.current_player = player1
        self.other_player = player2
        self.winner = None
        self.steps = 0

        # Configure logging
        logging.basicConfig(filename='logs/game.log',format='%(asctime)s - %(levelname)s - %(message)s',filemode='a',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        
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
                x, y = self.current_player.make_move()
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
        self.board[x][y] = self.current_player.name

    def switch_player(self):
        self.current_player, self.other_player = self.other_player, self.current_player

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

    def play_game(self):
        while self.winner is None and not self.is_board_full():
            self.display_board()

            x, y = self.input_move()

            self.update_board(x, y)
            self.switch_player()
            self.steps += 1

            self.winner = self.get_winner()

        self.display_result()

    def display_result(self):
        self.display_board()
        if self.winner:
            print(f'Player {self.winner} wins in {self.steps} steps!')
            self.log_winner()
        else:
            print("It's a draw.")
            self.log_draw()

    def log_winner(self):
        logging.info(f'{self.current_player.name} vs {self.other_player.name} - Winner: {self.winner} - Steps: {self.steps}')

    def log_draw(self):
        logging.info(f'{self.current_player.name} vs {self.other_player.name} - Draw')


if __name__ == "__main__":
    player1_name = input('Enter name for Player 1: ')
    player1 = Human(player1_name)

    player2_name = input('Enter name for Player 2 (or Bot): ')
    if player2_name.lower() == 'bot':
        player2 = Bot('Bot')
    else:
        player2 = Human(player2_name)

    game = TicTacToe(player1, player2)
    game.play_game()