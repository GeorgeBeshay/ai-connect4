class MinimaxWithAlphaBeta:

    # TODO: make state of type state

    def __init__(self, k: int):
        self.k = k
        self.explored = {}

    def run_minimax_with_alpha_beta(self, initial_state):
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

        return next_step

    def value(self, state, level: int, alpha: float, beta: float) -> float:
        if state.get_value() in self.explored:
            return self.explored[state.get_value()]

        evaluated_value = 0
        if level == self.k:
            if state.get_value() not in self.explored:
                # evaluated_value = get_evaluation(state)
                self.explored[state.get_value()] = evaluated_value
                return evaluated_value
            else:
                return self.explored[state.get_value()]

        if state.is_max():
            evaluated_value = self.max_value(state, level, alpha, beta)
        else:
            evaluated_value = self.min_value(state, level, alpha, beta)

        self[state.get_value()] = evaluated_value
        return evaluated_value

    def min_value(self, state, level: int, alpha: float, beta: float) -> float:
        v = float('inf')
        successors = state.get_successors()
        for successor in successors:
            v = min(v, self.value(successor, level + 1, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    def max_value(self, state, level: int, alpha: float, beta: float) -> float:
        v = - float('inf')
        successors = state.get_successors()
        for successor in successors:
            v = max(v, self.value(successor, level + 1, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
