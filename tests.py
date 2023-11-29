import unittest
from cli import TicTacToe, Human, Bot

class TestLogic(unittest.TestCase):

    def test_initialize_game_empty_board(self):
        # Test if the game is initialized with an empty board
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        self.assertEqual(game.board, [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])

    def test_switch_player(self):
        # Test if switching players works correctly
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        current_player = game.current_player
        game.switch_player()
        switched_player = game.current_player
        self.assertNotEqual(current_player, switched_player)

    def test_is_valid_move(self):
        # Test if valid moves are correctly identified
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        game.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, None],
        ]
        self.assertTrue(game.is_valid_move(1, 2))  # Valid move
        self.assertFalse(game.is_valid_move(0, 0))  # Invalid move, position already taken

    def test_get_winner_horizontal(self):
        # Test winning condition in a horizontal row
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        game.board = [
            ['X', 'X', 'X'],
            ['O', 'O', None],
            [None, None, None],
        ]
        game.winner = game.get_winner()
        self.assertEqual(game.winner, 'X')

    def test_get_winner_vertical(self):
        # Test winning condition in a vertical column
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        game.board = [
            ['X', 'O', None],
            ['X', 'O', None],
            ['X', None, None],
        ]
        game.winner = game.get_winner()
        self.assertEqual(game.winner, 'X')

    def test_get_winner_diagonal(self):
        # Test winning condition in a diagonal line
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        game.board = [
            ['O', 'X', 'X'],
            ['O', 'O', None],
            ['X', None, 'O'],
        ]
        game.winner = game.get_winner()
        self.assertEqual(game.winner, 'O')

    def test_get_winner_no_winner(self):
        # Test when there is no winner
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        game.winner = game.get_winner()
        self.assertIsNone(game.winner)

    def test_get_winner_empty_board(self):
        # Test when the board is empty, there should be no winner
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        game.winner = game.get_winner()
        self.assertIsNone(game.winner)

    def test_get_winner_draw(self):
        # Test when the game ends in a draw
        player1 = Human("Player1")
        player2 = Bot("Bot")
        game = TicTacToe(player1, player2)
        game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        game.winner = game.get_winner()
        self.assertIsNone(game.winner)


if __name__ == '__main__':
    unittest.main()