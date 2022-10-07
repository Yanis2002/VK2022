import unittest

from main import check_winner, make_move, check_draw
class TestN(unittest.TestCase):
    def test_check_winner(self):
        self.assertTrue(check_winner([['X', '', ''], ['X', '', ''], ['X', '', '']])) # vert 1
        self.assertTrue(check_winner([['', 'X', ''], ['', 'X', ''], ['', 'X', '']])) # vert 2
        self.assertTrue(check_winner([['', '', 'X'], ['', '', 'X'], ['', '', 'X']])) # vert 3
        self.assertTrue(check_winner([['X', 'X', 'X'], ['', '', ''], ['', '', '']])) # gor 1
        self.assertTrue(check_winner([['', '', ''], ['X', 'X', 'X'], ['', '', '']])) # gor 2
        self.assertTrue(check_winner([['', '', ''], ['', '', ''], ['X', 'X', 'X']])) #gor 3
        self.assertTrue(check_winner([['X', '', ''], ['', 'X', ''], ['', '', 'X']])) # first dig
        self.assertTrue(check_winner([['', '', 'X'], ['', 'X', ''], ['X', '', '']])) #second dig
        self.assertFalse(check_winner([['X', '', ''], ['', 'X', ''], ['X', '', '']])) # no winner
    def test_check_input(self):
        self.assertTrue(make_move('X','s t',[['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'X', '']]))
        self.assertTrue(make_move('X','33 0',[['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'X', '']]))
        self.assertTrue(make_move('X','0 0',[['O', '', ''], ['', '', ''], ['', '', '']]))
        self.assertTrue(make_move('O','0 0',[['X', '', ''], ['', '', ''], ['', '', '']]))
    def test_check_draw(self):
        self.assertTrue(check_draw([['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'X', 'O']])) #full matrix
        self.assertFalse(check_draw([['X', 'X', 'O'], ['O', 'O', 'X'], ['X', 'X', '']])) # not done game


if __name__ == '__main__':
    unittest.main()
