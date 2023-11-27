import unittest

from src.utilities.get_score import get_game_score


class GetScoreTests(unittest.TestCase):
    def setUp(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]

    def test_score1(self):
        self.assertEqual((0, 0), get_game_score(self.state, 1, 2))

    def test_score2(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 2],
            [0, 2, 0, 2, 0, 0, 2],
            [0, 1, 0, 2, 2, 0, 2],
            [1, 1, 1, 1, 1, 1, 2],
            [1, 1, 2, 2, 1, 2, 2]
        ]

        self.assertEqual((3, 3), get_game_score(self.state, 1, 2))

    def test_score3(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 2, 0, 0, 2],
            [0, 2, 0, 2, 2, 0, 2],
            [0, 1, 0, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 2],
            [1, 1, 2, 2, 1, 2, 2]
        ]

        self.assertEqual((3, 5), get_game_score(self.state, 1, 2))

    def test_score4(self):
        self.state = [
            [1, 0, 0, 0, 0, 0, 2],
            [1, 1, 0, 2, 0, 0, 2],
            [0, 1, 0, 2, 2, 0, 2],
            [0, 1, 1, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 2],
            [1, 1, 2, 2, 1, 2, 2]
        ]

        self.assertEqual((7, 5), get_game_score(self.state, 1, 2))

    def test_score5(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0]
        ]

        self.assertEqual((2, 0), get_game_score(self.state, 1, 2))

    def test_score6(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0]
        ]

        self.assertEqual((2, 0), get_game_score(self.state, 1, 2))

    def test_score7(self):
        self.state = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 2, 0, 0],
            [1, 1, 1, 2, 2, 0, 0],
            [1, 1, 2, 2, 2, 0, 0]
        ]

        self.assertEqual((2, 0), get_game_score(self.state, 1, 2))
