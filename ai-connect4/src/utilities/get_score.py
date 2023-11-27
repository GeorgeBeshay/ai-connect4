from typing import *


def get_game_score(state: List[List[int]]) -> Tuple[int, int]:
    return get_computer_score(state), get_human_score(state)


def get_computer_score(state: List[List[int]]) -> int:
    score = 0
    computer = 1
    score += count_in_rows(state, computer)
    score += count_in_columns(state, computer)
    score += count_in_main_diagonals(state, computer)
    score += count_in_secondary_diagonals(state, computer)
    return score


def get_human_score(state: List[List[int]]) -> int:
    score = 0
    human = 2
    score += count_in_rows(state, human)
    score += count_in_columns(state, human)
    score += count_in_main_diagonals(state, human)
    score += count_in_secondary_diagonals(state, human)
    return score


def count_in_rows(state: List[List[int]], player: int) -> int:
    score = 0

    for i in range(len(state)):
        max_sequence = 0
        current_sequence = 0
        for j in range(len(state[0])):
            if state[i][j] == player:
                current_sequence += 1
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 0

        max_sequence = max(max_sequence, current_sequence)
        if max_sequence >= 4:
            score = max_sequence - 4 + 1

    return score


def count_in_columns(state: List[List[int]], player: int) -> int:
    score = 0

    for j in range(len(state[0])):
        max_sequence = 0
        current_sequence = 0
        for i in range(len(state)):
            if state[i][j] == player:
                current_sequence += 1
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 0

        max_sequence = max(max_sequence, current_sequence)
        if max_sequence >= 4:
            score = max_sequence - 4 + 1

    return score


def count_in_main_diagonals(state: List[List[int]], player: int) -> int:
    score = 0
    rows = len(state)
    cols = len(state[0])

    for turn in range(rows):
        current_sequence = 0
        max_sequence = 0
        i = turn
        j = 0
        while j < cols and i >= 0:
            if state[i][j] == player:
                current_sequence += 1
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 0
            j += 1
            i -= 1

        max_sequence = max(max_sequence, current_sequence)
        if max_sequence >= 4:
            score = max_sequence - 4 + 1

    for turn in range(1, cols):
        current_sequence = 0
        max_sequence = 0
        i = rows - 1
        j = turn
        while i >= 0 and j < cols:
            if state[i][j] == player:
                current_sequence += 1
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 0
            i -= 1
            j += 1

        max_sequence = max(max_sequence, current_sequence)
        if max_sequence >= 4:
            score = max_sequence - 4 + 1
    return score


def count_in_secondary_diagonals(state: List[List[int]], player: int) -> int:
    score = 0
    rows = len(state)
    cols = len(state[0])

    for turn in range(rows):
        current_sequence = 0
        max_sequence = 0
        i = turn
        j = 0
        while j < cols and i < rows:
            if state[i][j] == player:
                current_sequence += 1
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 0
            i += 1
            j += 1

        max_sequence = max(max_sequence, current_sequence)
        if max_sequence >= 4:
            score = max_sequence - 4 + 1

    for turn in range(1, cols):
        current_sequence = 0
        max_sequence = 0
        i = 0
        j = turn
        while i < rows and j < cols:
            if state[i][j] == player:
                current_sequence += 1
            else:
                max_sequence = max(max_sequence, current_sequence)
                current_sequence = 0
            i += 1
            j += 1

        max_sequence = max(max_sequence, current_sequence)
        if max_sequence >= 4:
            score = max_sequence - 4 + 1
    return score
