import unittest
from src.state.state import State, _check_valid_indices, _get_cell_shift

WIDTH = 7
HEIGHT = 6


class TestStateMethods(unittest.TestCase):
    def setUp(self):
        # Initialize a State object with a known configuration for testing
        self.state = State()
        ''' 
        Assume computer = 1, Human = 2, Empty = 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        0 0 0 0 0 0 0
        '''

    def test_state_height_manipulation(self):
        """
            Test for manipulating the height of the columns within the state.

            This test method checks whether the height manipulation functions (_update_col and _get_height)
            work correctly by updating certain columns and verifying their heights.

            - Add discs to certain columns.
            - Check the height of these columns.
        """
        self.state.update_col(0, True)
        self.state.update_col(0, True)
        self.state.update_col(2, True)
        self.state.update_col(6, True)
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

    def test_state_full_height(self):
        """
            Test to fill the state entirely to maximum height.

            This test method fills the state entirely and checks whether each column reaches its maximum height.
            And, it verifies the entire state representation after it's been filled to the maximum height.
            Also, it verifies that adding any more discs to any columns will raise an exception.
        """
        for _ in range(HEIGHT):
            for col in range(WIDTH):
                self.state.update_col(col, True)
        '''
            1 2 1 2 1 2 1
            2 1 2 1 2 1 2
            1 2 1 2 1 2 1
            2 1 2 1 2 1 2
            1 2 1 2 1 2 1
            2 1 2 1 2 1 2
        '''
        for col in range(WIDTH):
            self.assertEqual(self.state._get_height(col), HEIGHT, f"Column {col} height mismatch")
        self.assertEqual(self.state.to_2d(),
                         [
                             [1, 2, 1, 2, 1, 2, 1],
                             [2, 1, 2, 1, 2, 1, 2],
                             [1, 2, 1, 2, 1, 2, 1],
                             [2, 1, 2, 1, 2, 1, 2],
                             [1, 2, 1, 2, 1, 2, 1],
                             [2, 1, 2, 1, 2, 1, 2],
                         ])
        for col in range(WIDTH):
            with self.assertRaises(AssertionError):
                self.state.update_col(col)

    def test_valid_indices(self):
        """
            Test to check valid row and column indices.

            This test method verifies that providing valid row and column indices within the board's range
            doesn't raise any AssertionErrors from the _check_valid_indices method.
        """
        # Test valid indices
        self.assertIsNone(_check_valid_indices(3, 4))  # Valid indices

    def test_invalid_row_index(self):
        """
            Test for an invalid row index.

            This test method checks whether an invalid row index (out of range) raises an AssertionError
            when passed to the _check_valid_indices method.
        """
        # Test invalid row index
        with self.assertRaises(AssertionError):
            _check_valid_indices(7, 4)  # Row index out of range

    def test_invalid_col_index(self):
        # Test invalid column index
        with self.assertRaises(AssertionError):
            _check_valid_indices(3, 8)  # Column index out of range

    def test_both_invalid_indices(self):
        # Test both invalid indices
        with self.assertRaises(AssertionError):
            _check_valid_indices(10, 8)  # Both row and column indices out of range

    def test_boundary_invalid_indices(self):
        """
            Test for boundary invalid indices.

            This test method checks whether providing row and column indices exactly at the boundary of the board
            (indices = board dimensions) raises an AssertionError when passed to the _check_valid_indices method.
        """
        # Test both invalid indices
        with self.assertRaises(AssertionError):
            _check_valid_indices(6, 7)  # Both row and column indices out of range

    def test_cell_shift_00(self):
        """
            Test for the bit shift calculation for cell (0, 0).

            This test method verifies the correctness of the bit shift calculation for cell (0, 0) using
            the _get_cell_shift method.
        """
        self.assertEqual(_get_cell_shift(0, 0), 63-3-6)

    def test_cell_shift_50(self):
        self.assertEqual(_get_cell_shift(5, 0), 63-3-1)

    def test_cell_shift_56(self):
        self.assertEqual(_get_cell_shift(5, 6), 5)

    def test_cell_value(self):
        """
            Test for retrieving cell values.

            This test method checks whether the _get_cell_val method correctly retrieves values from
            specific cells in the game board and returns the expected values. In addition to checking that the
            method throws exception with given misleading cell index.
        """
        self.state.update_col(3, True)
        self.assertEqual(self.state._get_cell_val(0, 3, True), 2)
        self.state.update_col(6, True)
        self.assertEqual(self.state._get_cell_val(0, 6, True), 1)
        self.assertEqual(self.state._get_cell_val(0, 5, True), 0)
        with self.assertRaises(AssertionError):
            self.state._get_cell_val(6, 7, True)

    def test_computer_turn(self):
        """
            Test for tracking the current player's turn.

            This test method checks whether the State class correctly tracks and returns the current player's turn.
        """
        self.assertFalse(self.state.is_computer_turn())
        self.state.update_col(3, True)
        self.assertTrue(self.state.is_computer_turn())
        self.state.update_col(0, True)
        self.assertFalse(self.state.is_computer_turn())
        self.state.update_col(5, True)
        self.assertTrue(self.state.is_computer_turn())
