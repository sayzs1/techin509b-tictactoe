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
    def test_get_winner(self):
        board = logic.make_empty_board()
        winner = logic.get_winner(board)
        if winner:
            print(f"Player {winner} wins!")
        else:
            print("It's a draw!")
    
    def test_make_empty_board(self):
        board = logic.make_empty_board()
        expected_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(board, expected_board)

    def test_other_player(self):
        # Test switching 'X' to 'O' and vice versa
        self.assertEqual(logic.other_player('X'), 'O')
        self.assertEqual(logic.other_player('O'), 'X')

if __name__ == '__main__':
    unittest.main()
