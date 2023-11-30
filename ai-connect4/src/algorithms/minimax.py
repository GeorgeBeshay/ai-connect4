import random
from typing import *
from src.state.state import State
from src.tree.tree_representation import Tree
from src.utilities.get_heuristic import calculate_heuristic

"""
Connect 4 Minimax Algorithm

This code defines an implementation of the Minimax algorithm for the Connect 4 game.

"""


class Minimax:
    def __init__(self, k: int):
        self.k = k
        self.explored = {}  # dictionary
        self.tree = None

    def run_minimax(self, initial_state: State) -> Tuple[float, State]:
        """

        Get the maximum value the computer can get from all its children

        :param initial_state: the initial state from which the algorithm runs
        :type initial_state: State

        :return: Tuple of the max value the computer can get and the state of next step
        """
        self.tree = Tree((initial_state.get_value(), 0))
        self.explored = {}
        successors = initial_state.get_successors()
        max_value = - float('inf')
        next_step = initial_state
        for successor in successors:
            current_value = self.value(successor, 1)
            self.tree.add_child_to_node(initial_state.get_value(), (successor.get_value(), current_value))
            if current_value > max_value:
                next_step = successor
                max_value = current_value

        self.tree.set_root((initial_state.get_value(), max_value))
        return max_value, next_step

    def value(self, state: State, level: int):
        """
        Calculate the value of state

        NOTE: there is explored map where it checks if this value of state has been explored before it returns its value
              otherwise, the value is computed and then stored in explored map to save time

        :param state: Current game state.
        :type state: State
        :param level: Current level in the search tree.
        :type level: int

        :return: Evaluated value of the current state.
        :rtype: int
        """

        if state.get_value() in self.explored:
            return self.explored[state.get_value()]

        evaluated_value = 0

        if level == self.k or len(state.get_successors()) == 0:  # terminal state
            evaluated_value = calculate_heuristic(state.to_2d(), 1, 2)
            self.explored[state.get_value()] = evaluated_value
            return evaluated_value
        if state.is_computer_turn():  # max
            evaluated_value = self.max_value(state, level)
        else:  # min
            evaluated_value = self.min_value(state, level)

        self.explored[state.get_value()] = evaluated_value
        return evaluated_value

    def max_value(self, state: State, level: int):
        """
        Function for the max player (computer).

        :param state: Current game state.
        :type state: State
        :param level: Current level in the search tree.
        :type level: int
        :return: Maximum evaluated value for the current state.
        :rtype: int
        """

        v = -float('inf')
        successors = state.get_successors()

        for successor in successors:
            child_value = self.value(successor, level + 1)

            self.tree.add_child_to_node(state.get_value(), (successor.get_value(), child_value))

            v = max(v, child_value)

        return v

    def min_value(self, state: State, level: int):
        """
        Function for the min player (player).

        :param state: Current game state.
        :type state: State
        :param level: Current level in the search tree.
        :type level: int
        :return: Minimum evaluated value for the current state.
        :rtype: int
        """
        v = float('inf')
        successors = state.get_successors()

        for successor in successors:
            child_value = self.value(successor, level + 1)

            self.tree.add_child_to_node(state.get_value(), (successor.get_value(), child_value))

            v = min(v, child_value)

        return v

# '''
# Assume computer = 1, Human = 2, Empty = 0
#     0 0 0 0 0 0 0
#     0 0 0 0 0 0 0
#     0 0 0 0 0 0 0
#     1 0 1 0 0 0 0
#     1 0 2 0 0 0 2
#     2 0 2 0 0 0 1
# '''
# trial_state = State()
# trial_state.update_col(0, True)
# trial_state.update_col(0, True)
# trial_state.update_col(2, True)
# trial_state.update_col(6, True)
# trial_state.update_col(2, True)
# trial_state.update_col(0, True)
# trial_state.update_col(6, True)


# k = 10
# minimax_with = Minimax(k)
# state = State(True, 0)
# print("trial state = ", state.to_2d())
# print("turn is comp: ", state.is_computer_turn())
# (a, step) = minimax_with.run_minimax(state)
# print(step.to_2d())
