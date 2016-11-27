import unittest
import tic_tac_toe


class TestTicTacToe(unittest.TestCase):

    def test_who_won_1_horizontal(self):
        # Given
        board = [[1, 1, 1], [2, 1, 0], [0, 0, 2]]
        # When
        result = tic_tac_toe.who_won(board)
        # Then
        self.assertEqual(1, result)

    def test_who_won_2_vertical(self):
        # Given
        board = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
        # When
        result = tic_tac_toe.who_won(board)
        # Then
        self.assertEqual(2, result)

    def test_who_won_1_vertical(self):
        # Given
        board = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
        # When
        result = tic_tac_toe.who_won(board)
        # Then
        self.assertEqual(1, result)

    def test_who_won_1_diagonal(self):
        # Given
        board = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
        # When
        result = tic_tac_toe.who_won(board)
        # Then
        self.assertEqual(1, result)

    def test_who_won_no_winner(self):
        # Given
        board = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
        # When
        result = tic_tac_toe.who_won(board)
        # Then
        self.assertEqual(0, result)

    def test_translate_move_converts_to_int_and_subtracts_index(self):
        # Given
        move = "3,2"
        # When
        result = tic_tac_toe.translate_move(move)
        # Then
        self.assertEqual(2, result[0])
        self.assertEqual(1, result[1])

if __name__ == '__main__':
    unittest.main()
