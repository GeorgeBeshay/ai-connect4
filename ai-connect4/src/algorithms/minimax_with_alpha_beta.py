from typing import *
from src.state.state import State
from src.tree.tree_representation import Tree
from src.utilities.get_heuristic import calculate_heuristic


class MinimaxWithAlphaBeta:

    def __init__(self, k: int):
        self.k = k
        self.explored = {}
        self.tree = None

    def run_minimax_with_alpha_beta(self, initial_state: State) -> Tuple[float, State]:
        """

        Get the maximum value the computer can get from all its children

        :param initial_state: the initial state from which the algorithm runs
        :type initial_state: State

        :return: Tuple of the max value the computer can get and the state of next step
        """
        self.tree = Tree((initial_state.get_value(), 0))
        self.explored = {}
        successors = initial_state.get_successors()
        alpha = - float('inf')
        beta = float('inf')
        next_step = initial_state
        for successor in successors:
            current_value = self.value(successor, 1, alpha, beta)
            self.tree.add_child_to_node(initial_state.get_value(), (successor.get_value(), current_value))
            if current_value > alpha:
                next_step = successor
                alpha = current_value

        self.tree.set_root((initial_state.get_value(), alpha))
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
        if level == self.k or len(state.get_successors()) == 0:  # terminal state
            evaluated_value = calculate_heuristic(state.to_2d(), 1, 2)
            self.explored[state.get_value()] = evaluated_value
            return evaluated_value

        if state.is_computer_turn():
            evaluated_value = self.max_value(state, level, alpha, beta)
        else:
            evaluated_value = self.min_value(state, level, alpha, beta)

        self.explored[state.get_value()] = evaluated_value
        return evaluated_value

    def min_value(self, state: State, level: int, alpha: float, beta: float) -> float:
        v = float('inf')
        successors = state.get_successors()

        for successor in successors:
            child_value = self.value(successor, level + 1, alpha, beta)

            self.tree.add_child_to_node(state.get_value(), (successor.get_value(), child_value))

            v = min(v, child_value)

            if v <= alpha:
                return v

            beta = min(beta, v)
        return v

    def max_value(self, state: State, level: int, alpha: float, beta: float) -> float:
        v = - float('inf')
        successors = state.get_successors()

        for successor in successors:
            child_value = self.value(successor, level + 1, alpha, beta)

            self.tree.add_child_to_node(state.get_value(), (successor.get_value(), child_value))

            v = max(v, child_value)

            if v >= beta:
                return v

            alpha = max(alpha, v)

        return v


# k = 13
# minimax_with = MinimaxWithAlphaBeta(k)
# state = State(True, 0)
# print("trial state = ", state.to_2d())
# print("turn is comp: ", state.is_computer_turn())
# (a, step) = minimax_with.run_minimax_with_alpha_beta(state)
# print(step.to_2d())
