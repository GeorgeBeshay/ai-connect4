from typing import *
from src.state.state import State
from src.tree.treeRepresentation import print_tree

class MinimaxWithAlphaBeta:

    def __init__(self, k: int):
        self.k = k
        self.explored = {}
        self.tree = {}

    def run_minimax_with_alpha_beta(self, initial_state: State) -> Tuple[float, State]:
        """

        Get the maximum value the computer can get from all its children

        :param initial_state: the initial state from which the algorithm runs
        :type initial_state: State

        :return: Tuple of the max value the computer can get and the state of next step
        """
        self.explored = {}
        successors = initial_state.get_successors()
        alpha = - float('inf')
        beta = float('inf')
        next_step = initial_state
        for successor in successors:
            current_value = self.value(successor, 1, alpha, beta)
            if current_value > alpha:
                next_step = successor
                alpha = current_value

        return alpha, next_step

    def value(self, state: State, level: int, alpha: float, beta: float) -> float:
        """
        Calculate the value of state

        NOTE: there is explored map where it checks if this value of state has been seen before it returns its value
              otherwise, the value is computed and then stored in explored map

        :param state: the current state
        :type state: State
        :param level: the level or the depth of this state
        :type level: int
        :param alpha: the maximum value, this state has seen
        :type alpha: float
        :param beta: the minimum value, this state has seen
        :type beta: float
        :return: the value of this state
        """
        if state.get_value() in self.explored:
            return self.explored[state.get_value()]

        evaluated_value = 0
        if level == self.k:
            if state.get_value() not in self.explored:
                # evaluated_value = get_evaluation(state)
                # evaluated_value = get_computer_score(state.to_2d())
                self.explored[state.get_value()] = evaluated_value
                return evaluated_value
            else:
                return self.explored[state.get_value()]
        # print(state.to_2d())
        # print(state.is_computer_turn())
        if state.is_computer_turn():
            evaluated_value = self.max_value(state, level, alpha, beta)
        else:
            evaluated_value = self.min_value(state, level, alpha, beta)

        self.explored[state.get_value()] = evaluated_value
        return evaluated_value

    def min_value(self, state: State, level: int, alpha: float, beta: float) -> float:
        v = float('inf')
        # print("In min: ")
        successors = state.get_successors()
        self.tree[state.get_value()] = {"value": v, "children": {}}
        for successor in successors:
            child_value = self.value(successor, level + 1, alpha, beta)
            v = min(v, child_value)
            self.tree[state.get_value()]["children"][successor.get_value()] = {"value": child_value}
            if v <= alpha:
                self.tree[state.get_value()]["value"] = v
                return v
            beta = min(beta, v)
        self.tree[state.get_value()]["value"] = v
        return v

    def max_value(self, state: State, level: int, alpha: float, beta: float) -> float:
        v = - float('inf')
        # print("In max: ")
        successors = state.get_successors()
        self.tree[state.get_value()] = {"value": v, "children": {}}
        for successor in successors:
            child_value = self.value(successor, level + 1, alpha, beta)
            v = max(v, child_value)
            self.tree[state.get_value()]["children"][successor.get_value()] = {"value": child_value}
            if v >= beta:
                self.tree[state.get_value()]["value"] = v
                return v
            alpha = max(alpha, v)
        self.tree[state.get_value()]["value"] = v
        return v

k = 4
minimax = MinimaxWithAlphaBeta(k)
state = State(True, 0)
(a, step) = minimax.run_minimax_with_alpha_beta(state)
print_tree(minimax.tree,0)
# print(a)
# print(step.to_2d())