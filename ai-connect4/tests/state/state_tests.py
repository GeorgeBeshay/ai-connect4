import unittest
from src.state.state import State


class TestStateMethods(unittest.TestCase):
    def setUp(self):
        # Initialize a State object with a known configuration for testing
        self.state = State(7, 6, is_computer_turn=False)
        ''' Assume computer = 1, Human = 2, Empty = 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        '''

    def test_state_manipulation(self):
        self.state._update_col(0, True)
        self.state._update_col(0, True)
        self.state._update_col(2, True)
        self.state._update_col(6, True)
        '''
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        1 0 0 0 0 0 0
        2 0 2 0 0 0 1
        '''
        self.assertEqual(self.state._get_height(0), 2, f"Column {0} height mismatch")
        self.assertEqual(self.state._get_height(2), 1, f"Column {2} height mismatch")
        self.assertEqual(self.state._get_height(6), 1, f"Column {6} height mismatch")
        print('\n'.join([' '.join(map(str, row)) for row in self.state.to_2d()]))
