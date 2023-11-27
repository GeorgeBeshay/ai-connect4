from typing import *


# First number for computer score and the second number for human score
def get_game_score(state: List[List[int]], computer_number: int, human_number: int) -> Tuple[int, int]:
    return get_player_score(state, computer_number), get_player_score(state, human_number)


def get_player_score(state: List[List[int]], player_number: int) -> int:
    score = 0
    score += count_in_rows(state, player_number)
    score += count_in_columns(state, player_number)
    score += count_in_main_diagonals(state, player_number)
    score += count_in_secondary_diagonals(state, player_number)
    return score


def count_in_rows(state: List[List[int]], player: int) -> int:
    score = 0

    for i in range(len(state)):
        current_sequence = 0
        for j in range(len(state[0])):
            if state[i][j] == player:
                current_sequence += 1
                if current_sequence >= 4:
                    score += 1
            else:
                current_sequence = 0

    return score


def count_in_columns(state: List[List[int]], player: int) -> int:
    score = 0

    for j in range(len(state[0])):
        current_sequence = 0
        for i in range(len(state)):
            if state[i][j] == player:
                current_sequence += 1
                if current_sequence >= 4:
                    score += 1
            else:
                current_sequence = 0

    return score


def count_in_main_diagonals(state: List[List[int]], player: int) -> int:
    score = 0
    rows = len(state)
    cols = len(state[0])

    for turn in range(rows):
        score += _in_main_diagonals(state, player, turn, 0)

    for turn in range(1, cols):
        score += _in_main_diagonals(state, player, rows - 1, turn)

    return score


def _in_main_diagonals(state: List[List[int]], player: int, i: int, j: int) -> int:
    score = 0
    cols = len(state[0])
    current_sequence = 0
    while j < cols and i >= 0:
        if state[i][j] == player:
            current_sequence += 1
            if current_sequence >= 4:
                score += 1
        else:
            current_sequence = 0
        j += 1
        i -= 1

    return score


def count_in_secondary_diagonals(state: List[List[int]], player: int) -> int:
    score = 0
    rows = len(state)
    cols = len(state[0])

    for turn in range(rows):
        score += _in_secondary_diagonals(state, player, turn, 0)

    for turn in range(1, cols):
        score += _in_secondary_diagonals(state, player, 0, turn)

    return score


def _in_secondary_diagonals(state: List[List[int]], player: int, i: int, j: int) -> int:
    score = 0
    current_sequence = 0
    rows = len(state)
    cols = len(state[0])

    while j < cols and i < rows:
        if state[i][j] == player:
            current_sequence += 1
            if current_sequence >= 4:
                score += 1
        else:
            current_sequence = 0
        i += 1
        j += 1

    return score
