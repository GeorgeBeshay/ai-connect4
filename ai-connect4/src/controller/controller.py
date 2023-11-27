from src.state.state import State, change_game_board


class Connect4Controller:
    """
    Class representing a Connect 4 game controller.
    """

    def __init__(self, wid, ht):
        """
        Initialize the Connect 4 game controller.

        Initializes the game_state attribute using the State class.
        """
        change_game_board(wid, ht)
        self.game_state = State()

    def play(self, col):
        """
        Play a move in the Connect 4 game.

        Args:
            col (int): The column in which the player wants to place their piece.

        Returns:
            list: A 2D list representing the updated game state after the move.
        """
        self.game_state.update_col(col, True)
        return self.game_state.to_2d()

    def get_board(self):
        return self.game_state.to_2d()
