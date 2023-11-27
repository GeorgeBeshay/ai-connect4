import random

from src.state.state import State
from src.tree.treeRepresentation import print_tree
"""
Connect 4 Minimax Algorithm

This code defines an implementation of the Minimax algorithm for the Connect 4 game.

"""


class Minimax:
    def __init__(self, k: int):
        self.k = k
        self.explored = {}  # dictionary
        self.tree = {}

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
        # print("is the turn of computer: ", state.is_computer_turn())
        # print("state.value = ",state.get_value())

        if state.get_value() in self.explored:
            return self.explored[state.get_value()]

        evaluated_value = 0

        if level == self.k:  # terminal state
            # TODO: evaluate the state
            # evaluated_value = get_evaluation(state)
            # evaluated_value = get_computer_score(state.to_2d())
            evaluated_value = random.randint(-100,100)
            # print("evaluated_value = ", evaluated_value)
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
        # print("In max")
        v = -float('inf')
        successors = state.get_successors()
        self.tree[state.get_value()] = {"value": v, "children": {}}
        for successor in successors:
            child_value = self.value(successor, level + 1)
            v = max(v, child_value)
            self.tree[state.get_value()]["children"][successor.get_value()] = {"value": child_value}
        self.tree[state.get_value()]["value"] = v
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
        # print("In min")
        v = float('inf')
        successors = state.get_successors()
        self.tree[state.get_value()] = {"value": v, "children": {}}
        for successor in successors:
            child_value = self.value(successor, level + 1)
            v = min(v, child_value)
            self.tree[state.get_value()]["children"][successor.get_value()] = {"value": child_value}
        self.tree[state.get_value()]["value"] = v
        return v

    # def print_tree(self, node, indent):
    #     """
    #     Print the Minimax tree.
    #
    #     :param node: Current node in the tree.
    #     :type node: dict
    #     :param indent: Current indentation level.
    #     :type indent: int
    #     """
    #
    #     for key, value in node.items():
    #         print("  " * indent, key, ":", value["value"])
    #         if "children" in value:
    #             self.print_tree(value["children"], indent + 1)

'''
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    0 0 0 0 0 0 0
    1 0 2 0 0 0 0
    2 0 2 0 0 0 1
'''
trial_state = State()
trial_state.update_col(0, True)
trial_state.update_col(0, True)
trial_state.update_col(2, True)
trial_state.update_col(6, True)
trial_state.update_col(2, True)
k = 3
minimax_instance = Minimax(k)
result = minimax_instance.value(trial_state, 0)
print("Result = ", result)
# Print the Minimax tree
print_tree(minimax_instance.tree,0)