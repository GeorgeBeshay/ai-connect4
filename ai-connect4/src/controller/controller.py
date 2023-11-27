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

        :return: list: A 2D list representing the updated game state after the move.
        """
        try:
            self.game_state.update_col(col, True)
        except AssertionError as err:
            print("Oops .. Invalid Indices !!")
        return self.game_state.to_2d()

    def get_board(self):
        """
        Returns the 2D decimal representation of the game board

        :return: list: A 2D list representing the updated game state after the move.
        """
        return self.game_state.to_2d()

    def get_state(self):
        """
        Returns the current game state object.

        :return: State: The current game state object
        """
        return self.game_state
