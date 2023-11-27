"""
Connect 4 Game State Management Module

This module manages the state of a Connect 4 game, providing functions and a class (`State`) to handle the game's
internal representation, validation, and transformation.

Module Functions:
    - Public Methods:
        - `change_game_board`: Updates the global game board dimensions.
    - Private Methods:
        - `_check_valid_indices`: Validates row and column indices for the game board.
        - `_get_cell_shift`: Computes the bit shift for a specific cell in the game state.

Class:
- `State`: Represents the state of the Connect 4 game.
    - `__init__`: Initializes the game state.
    - `get_successors`: Generates possible successor states.
    - `to_2d`: Converts the internal state representation to a 2D array.
    - `is_computer_turn`: Returns the current state turn player.
    - `update_col`: Updates the game state based on a selected column.

Private Methods (in the State class):
- `_update_height`: Manages the internal representation of column heights.
- `_get_height`: Retrieves the height of a column.
- `_get_cell_val`: Retrieves the value of a specific cell.

This module provides essential functionalities for managing the game state,
validating moves, and transforming the state representation for Connect 4 gameplay.

PS: Kindly note that in the game board representation in case of decimal integers, we chose to represent the empty cell
by a 0 value, while the computer and player discs with 1 and 2 values respectively.
"""


import math

WIDTH = 7
HEIGHT = 6


# Public
def change_game_board(wid, ht):
    """
        Updates the global game board dimensions.

        :param wid: New width for the game board.
        :type wid: int
        :param ht: New height for the game board.
        :type ht: int
    """
    global WIDTH, HEIGHT
    WIDTH = wid
    HEIGHT = ht


class State:
    def __init__(self, comp_turn=False, state_val=0):
        """
            Initializes the game state.

            :param comp_turn: Flag indicating the current player's turn. Defaults to False.
            :type comp_turn: bool
            :param state_val: Initial state representation. Defaults to 0.
            :type state_val: int
        """
        self.value = state_val
        self.comp_turn = comp_turn
        # State = [h0 C0 C1 ... C H-1 ... h W-1 C0 C1 ... C H-1] bits
        # Total_bits = width * height + width * math.ceil(math.log2(height + 1))

    # ---------------------- Public Methods ----------------------
    def update_col(self, col, change_turn=False):
        """
            Updates the game state based on a selected column.

            This method simulates a move by a player, updating the game state
            and modifying the internal representation accordingly.

            :param col: Column index.
            :type col: int
            :param change_turn: Flag to change the player's turn. Defaults to False.
            :type change_turn: bool
        """
        row = self._get_height(col)
        _check_valid_indices(row, col)

        cell_index = _get_cell_shift(row, col)
        mask = 1 << cell_index

        if not self.comp_turn:
            self.value |= mask  # Set the bit to 1
        else:
            self.value &= ~mask  # Set the bit to 0

        self._update_height(col)

        if change_turn:
            self.comp_turn = not self.comp_turn

    def get_successors(self):
        """
            Generates possible successor states.

            :return: List of possible successor states.
            :rtype: list
        """
        successors = []
        for col_idx in range(WIDTH):
            try:
                temp_state = State(state_val=self.value, comp_turn=self.is_computer_turn())
                temp_state.update_col(col_idx, True)
                successors.append(temp_state)
            except AssertionError:
                pass
        return successors

    def to_2d(self):
        """
            Converts the internal state representation to a 2D array.

            :return: 2D representation of the game state.
            :rtype: list
        """
        state_2d = []
        for row_idx in range(HEIGHT - 1, -1, -1):
            state_2d.append([])
            for col_idx in range(WIDTH):
                state_2d[-1].append(self._get_cell_val(row_idx, col_idx, True))
        # print('\n'.join([' '.join(map(str, row)) for row in state_2d]))
        return state_2d

    def is_computer_turn(self):
        """
            Returns the current state turn player.

            :return: True if it's the computer's turn, False otherwise.
            :rtype: bool
        """
        return self.comp_turn

    # ---------------------- Private Methods ----------------------
    def _update_height(self, col):
        """
            Manages the internal representation of column heights.

            This method handles the logic for keeping track of the column heights
            within the game board's internal representation.

            :param col: Column index.
            :type col: int
        """
        mirrored_col = WIDTH - 1 - col  # 0 => 3 ,, 1 => 2 etc..
        h_i_bits_count = math.ceil(math.log2(HEIGHT + 1))  # e.g. 3 bits
        shift_len = HEIGHT + (mirrored_col * (h_i_bits_count + HEIGHT))
        self.value += (1 << shift_len)

    def _get_height(self, col):
        """
            Retrieves the height of a column.

            This method determines the height of a specific column
            based on the internal representation.

            :param col: Column index.
            :type col: int

            :return: Height of the specified column.
            :rtype: int
        """
        # User see board columns indices as: 0 1 2 3
        # Integer Representation see board columns indices as: 3 2 1 0
        h_i_bits_count = math.ceil(math.log2(HEIGHT + 1))  # e.g. 3 bits
        h_i_bits = (1 << h_i_bits_count) - 1  # e.g. if 3 bits => 111
        shift_len = HEIGHT + _get_cell_shift(0, col)
        h_i = ((h_i_bits << shift_len) & self.value) >> shift_len
        return h_i

    def _get_cell_val(self, row, col, in_decimal=False):    # 0 > empty, 1 > computer, 2 > person
        """
            Retrieves the value of a specific cell.

            This method fetches the value of a cell in the Connect 4 game board.
            It provides the state of the cell in terms of the player occupying it, where in case of decimal
            representation, the values 0, 1, 2 indicates that the cell is either empty or occupied by the computer
            or occupied by the player, respectively. In case of binary representation, a refer to the column height
            will be needed.

            :param row: Row index.
            :type row: int
            :param col: Column index.
            :type col: int
            :param in_decimal: Flag to return values in decimal. Defaults to False.
            :type in_decimal: bool

            :return: Value of the specified cell.
            :rtype: int
        """
        cell_shift = _get_cell_shift(row, col)
        val = (self.value & (1 << cell_shift)) >> cell_shift
        if in_decimal:
            if row < self._get_height(col):
                if val:
                    val = 2
                else:
                    val = 1
            else:
                val = 0
        return val


# Private
def _check_valid_indices(row, col):
    """
        Validates row and column indices for the game board.

        This function ensures that the provided row and column indices
        fall within the acceptable range for the game board dimensions.

        :param row: Row index.
        :type row: int
        :param col: Column index.
        :type col: int
    """
    assert 0 <= row < HEIGHT and 0 <= col < WIDTH, "Invalid cell was given"
    return


def _get_cell_shift(row, col):
    """
        Computes the bit shift for a specific cell in the game state.

        This function calculates the bit shift required to access a particular cell in the game state representation.
        It depends on the state integer representation, that has the notation of
        [h_0 c_0 c_1 ... c_H-1 ... h_W-1 c_0 c_1 ... h_W-1], we can notice the total number of bits required to be
        shifted is equal to the total bits needed to represent the upcoming columns (to the right) as the actual
        integer indexing starts from the least-significant bit, that is the right most one. In addition to the bits
        required to store the rows before the indicated row (that is, the discs coming below the indicated row)

        :param row: Row index.
        :type row: int
        :param col: Column index.
        :type col: int

        :return: Bit shift value.
        :rtype: int
    """
    _check_valid_indices(row, col)
    mirrored_col = WIDTH - 1 - col  # 0 => 3 ,, 1 => 2 etc..
    h_i_bits_count = math.ceil(math.log2(HEIGHT + 1))  # e.g. 3 bits
    return mirrored_col * (HEIGHT + h_i_bits_count) + row
