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

Private Methods (in the State class):
- `_update_col`: Updates the game state based on a selected column.
- `_update_height`: Manages the internal representation of column heights.
- `_get_height`: Retrieves the height of a column.
- `_get_cell_val`: Retrieves the value of a specific cell.

This module provides essential functionalities for managing the game state,
validating moves, and transforming the state representation for Connect 4 gameplay.
"""


import math

WIDTH = 7
HEIGHT = 6


# Public
def change_game_board(wid, ht):
    global WIDTH, HEIGHT
    WIDTH = wid
    HEIGHT = ht


class State:
    def __init__(self, width, height, is_computer_turn, state=0):
        self.value = state
        self.is_computer_turn = is_computer_turn
        # State = [h0 C0 C1 ... C H-1 ... h W-1 C0 C1 ... C H-1] bits
        # Total_bits = width * height + width * math.ceil(math.log2(height + 1))

    # ---------------------- Public Methods ----------------------
    def get_successors(self):
        successors = []
        for col_idx in range(WIDTH):
            try:
                temp_state = State(WIDTH, HEIGHT, not self.is_computer_turn)
                temp_state._update_col(col_idx)
                successors.append(temp_state)
            except AssertionError:
                pass

    def to_2d(self):
        state_2d = []
        for row_idx in range(HEIGHT - 1, -1, -1):
            state_2d.append([])
            for col_idx in range(WIDTH):
                state_2d[-1].append(self._get_cell_val(row_idx, col_idx, True))
        return state_2d

    def is_computer_turn(self):
        return self.is_computer_turn

    # ---------------------- Private Methods ----------------------
    def _update_col(self, col, change_turn=False):
        row = self._get_height(col)
        _check_valid_indices(row, col)

        cell_index = _get_cell_shift(row, col)
        mask = 1 << cell_index

        if not self.is_computer_turn:
            self.value |= mask  # Set the bit to 1
        else:
            self.value &= ~mask  # Set the bit to 0

        self._update_height(col)

        if change_turn:
            self.is_computer_turn = not self.is_computer_turn

    def _update_height(self, col):
        mirrored_col = WIDTH - 1 - col  # 0 => 3 ,, 1 => 2 etc..
        h_i_bits_count = math.ceil(math.log2(HEIGHT + 1))  # e.g. 3 bits
        shift_len = HEIGHT + (mirrored_col * (h_i_bits_count + HEIGHT))
        self.value += (1 << shift_len)

    def _get_height(self, col):
        # User see board columns indices as: 0 1 2 3
        # Integer Representation see board columns indices as: 3 2 1 0
        h_i_bits_count = math.ceil(math.log2(HEIGHT + 1))  # e.g. 3 bits
        h_i_bits = (1 << h_i_bits_count) - 1  # e.g. if 3 bits => 111
        shift_len = HEIGHT + _get_cell_shift(0, col)
        h_i = ((h_i_bits << shift_len) & self.value) >> shift_len
        return h_i

    def _get_cell_val(self, row, col, in_decimal=False):    # 0 > empty, 1 > computer, 2 > person
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
    assert 0 <= row < HEIGHT and 0 <= col < WIDTH, "Invalid cell was given"
    return


def _get_cell_shift(row, col):
    _check_valid_indices(row, col)
    mirrored_col = WIDTH - 1 - col  # 0 => 3 ,, 1 => 2 etc..
    h_i_bits_count = math.ceil(math.log2(HEIGHT + 1))  # e.g. 3 bits
    return mirrored_col * (HEIGHT + h_i_bits_count) + row
