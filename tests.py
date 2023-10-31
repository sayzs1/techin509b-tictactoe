import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!
            # Test case 2: 'O' is the winner
        board = [
            ['X', 'O', 'X'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

        # Test case 3: No winner (draw)
        board = [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertIsNone(logic.get_winner(board))

    def test_make_empty_board(self):
        # Test that make_empty_board returns a valid empty board
        board = logic.make_empty_board()
        self.assertEqual(board, [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ])

    def test_other_player(self):
        # Test switching 'X' to 'O' and vice versa
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

if __name__ == '__main__':
    unittest.main()
