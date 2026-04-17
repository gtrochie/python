import unittest
from ttt import find_winner

class TestTicTacToe(unittest.TestCase):

    def test_row_winner(self):
        board = [
            ['X', 'X', 'X'],
            ['O', ' ', 'O'],
            [' ', ' ', ' ']
        ]
        self.assertEqual(find_winner(board), 'X')

    def test_column_winner(self):
        board = [
            ['O', 'X', ' '],
            ['O', ' ', ' '],
            ['O', 'X', 'X']
        ]
        self.assertEqual(find_winner(board), 'O')

    def test_diagonal_winner(self):
        board = [
            ['X', 'O', ' '],
            [' ', 'X', ' '],
            ['O', 'O', 'X']
        ]
        self.assertEqual(find_winner(board), 'X')

    def test_no_winner(self):
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertEqual(find_winner(board), None)

    def test_invalid_size(self):
        
        board = [['X', 'X'], ['O', 'O']]
        with self.assertRaises(ValueError):
            find_winner(board)

    def test_invalid_characters(self):
       
        board = [
            ['X', 'X', 'X'],
            ['O', 'O', 'Z'],
            [' ', ' ', ' ']
        ]
        with self.assertRaises(ValueError):
            find_winner(board)

if __name__ == '__main__':
    unittest.main()