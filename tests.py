import unittest
from logic import get_winner
from cli import TicTacToe

class TestLogic(unittest.TestCase):

    def test_initialize_game_empty_board(self):
        # Test if the game is initialized with an empty board
        game = TicTacToe()
        self.assertEqual(game.board, [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])

    def test_assign_players(self):
        # Test if players are assigned unique pieces X and O
        game = TicTacToe()
        player1, player2 = game.current_user, game.other_player()
        self.assertEqual(player1, 'O')
        self.assertEqual(player2, 'X')

    def test_switch_player(self):
        # Test if switching players works correctly
        game = TicTacToe()
        current_player = game.current_user
        game.switch_player()
        switched_player = game.current_user
        self.assertNotEqual(current_player, switched_player)

    def test_is_valid_move(self):
        # Test if valid moves are correctly identified
        game = TicTacToe()
        game.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, None, None],
        ]
        self.assertTrue(game.is_valid_move(1, 2))  # Valid move
        self.assertFalse(game.is_valid_move(0, 0))  # Invalid move, position already taken

    def test_get_winner_horizontal(self):
        # Test winning condition in a horizontal row
        board = [
            ['X', 'X', 'X'],
            ['O', 'O', None],
            [None, None, None],
        ]
        self.assertEqual(get_winner(board), 'X')

    def test_get_winner_vertical(self):
        # Test winning condition in a vertical column
        board = [
            ['X', 'O', None],
            ['X', 'O', None],
            ['X', None, None],
        ]
        self.assertEqual(get_winner(board), 'X')

    def test_get_winner_diagonal(self):
        # Test winning condition in a diagonal line
        board = [
            ['O', 'X', 'X'],
            ['O', 'O', None],
            ['X', None, 'O'],
        ]
        self.assertEqual(get_winner(board), 'O')

    def test_get_winner_no_winner(self):
        # Test when there is no winner
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertIsNone(get_winner(board))

    def test_get_winner_empty_board(self):
        # Test when the board is empty, there should be no winner
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertIsNone(get_winner(board))

    def test_get_winner_draw(self):
        # Test when the game ends in a draw
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertIsNone(get_winner(board))


if __name__ == '__main__':
    unittest.main()