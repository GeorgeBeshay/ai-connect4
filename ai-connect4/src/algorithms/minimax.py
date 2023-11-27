
class Minimax:
    def __init__(self, k: int):
        self.k = k
        self.explored = {}

    def value(self, state, level: int):
        if state.get_value() in self.explored:
            return self.explored[state.get_value()]

        evaluated_value = 0

        if level == self.k: # terminal state
            # TODO: evaluate the state
            # evaluate the value of the state which is the best achievable outcome from that state
            self.explored[state.get_value()] = evaluated_value
            return evaluated_value
        if state.is_computer_turn(): # max
            evaluated_value = self.max_value(state, level)
        else:
            evaluated_value = self.min_value(state, level)

        self[state.get_value()] = evaluated_value
        return evaluated_value

    def max_value(self, state, level :int):
        v = -float('inf')
        successors = state.get_successors()
        for successor in successors:
            v = max(v, self.value(successor, level + 1))
        return v

    def min_value(self, state, level :int):
        v = float('inf')
        successors = state.get_successors()
        for successor in successors:
            v = min(v, self.value(successor, level + 1))
        return v
