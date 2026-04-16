import unittest
from game import determine_winner

class TestRockPaperScissorsLizardSpock(unittest.TestCase):

    def test_draw(self):
        self.assertEqual(determine_winner('rock', 'rock'), 'Draw')
        self.assertEqual(determine_winner('paper', 'paper'), 'Draw')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'Draw')
        self.assertEqual(determine_winner('lizard', 'lizard'), 'Draw')
        self.assertEqual(determine_winner('spock', 'spock'), 'Draw')

    def test_user_wins_rock(self):
        self.assertEqual(determine_winner('rock', 'scissors'), 'user won')
        self.assertEqual(determine_winner('rock', 'lizard'), 'user won')

    def test_user_wins_paper(self):
        self.assertEqual(determine_winner('paper', 'rock'), 'user won')
        self.assertEqual(determine_winner('paper', 'spock'), 'user won')

    def test_user_wins_scissors(self):
        self.assertEqual(determine_winner('scissors', 'paper'), 'user won')
        self.assertEqual(determine_winner('scissors', 'lizard'), 'user won')

    def test_user_wins_lizard(self):
        self.assertEqual(determine_winner('lizard', 'spock'), 'user won')
        self.assertEqual(determine_winner('lizard', 'paper'), 'user won')

    def test_user_wins_spock(self):
        self.assertEqual(determine_winner('spock', 'scissors'), 'user won')
        self.assertEqual(determine_winner('spock', 'rock'), 'user won')

    def test_computer_wins(self):
        self.assertEqual(determine_winner('rock', 'paper'), 'computer won')
        self.assertEqual(determine_winner('rock', 'spock'), 'computer won')
        self.assertEqual(determine_winner('paper', 'scissors'), 'computer won')
        self.assertEqual(determine_winner('paper', 'lizard'), 'computer won')
        self.assertEqual(determine_winner('scissors', 'rock'), 'computer won')
        self.assertEqual(determine_winner('scissors', 'spock'), 'computer won')
        self.assertEqual(determine_winner('lizard', 'rock'), 'computer won')
        self.assertEqual(determine_winner('lizard', 'scissors'), 'computer won')
        self.assertEqual(determine_winner('spock', 'paper'), 'computer won')
        self.assertEqual(determine_winner('spock', 'lizard'), 'computer won')

    def test_case_insensitive(self):
        self.assertEqual(determine_winner('Rock', 'SCISSORS'), 'user won')
        self.assertEqual(determine_winner('PAPER', 'rock'), 'user won')

if __name__ == '__main__':
    unittest.main()