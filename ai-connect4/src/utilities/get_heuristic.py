from typing import List

from src.utilities.get_score import get_player_score
from src.state.state import _check_valid_indices


def get_boundary_pts(state):
    pts = []
    for row in range(len(state)):
        pts.append((row, 0))
        pts.append((row, len(state[0]) - 1))
    for col in range(1, len(state[0])):
        pts.append((0, col))
    return pts


def calc_row(state: List[List[int]], player_piece: int):
    score = 0
    for row in range(len(state)):
        accumulator = 0
        longest_chain = 0
        for col in range(len(state[0])):
            if state[row][col] == player_piece or state[row][col] == 0:
                if state[row][col] == player_piece:
                    accumulator += 1
                # accumulator += 1
                longest_chain += 1
            else:
                if longest_chain > 3:
                    score += (longest_chain - 3) * 25 * accumulator
                # score += (longest_chain - 3) * 100 - (longest_chain - accumulator) * 25
                accumulator = 0
                longest_chain = 0
        if longest_chain > 3:
            score += (longest_chain - 3) * 25 * accumulator
    return score


def calc_col(state: List[List[int]], player_piece: int):
    score = 0
    for col in range(len(state[0])):
        accumulator = 0
        longest_chain = 0
        for row in range(len(state)):
            if state[row][col] == player_piece or state[row][col] == 0:
                if state[row][col] == player_piece:
                    accumulator += 1
                # accumulator += 1
                longest_chain += 1
            else:
                if longest_chain > 3:
                    score += (longest_chain - 3) * 25 * accumulator
                # score += (longest_chain - 3) * 100 - (longest_chain - accumulator) * 25
                accumulator = 0
                longest_chain = 0
        if longest_chain > 3:
            score += (longest_chain - 3) * 25 * accumulator
    return score


def calc_diagonal(state: List[List[int]], player_piece: int):
    boundary_pts = get_boundary_pts(state)
    score = 0
    for pt in boundary_pts:
        # up left

        accumulator = 0
        longest_chain = 0
        i = 0
        # while _check_valid_indices(pt[0] - i, pt[1] - i):
        while (0 <= pt[0] - i) and (0 <= pt[1] - i):
            if state[pt[0] - i][pt[1] - i] == player_piece or state[pt[0] - i][pt[1] - i] == 0:
                if state[pt[0] - i][pt[1] - i] == player_piece:
                    accumulator += 1
                # accumulator += 1
                longest_chain += 1
            else:
                if longest_chain > 3:
                    score += (longest_chain - 3) * 25 * accumulator
                # score += (longest_chain - 3) * 100 - (longest_chain - accumulator) * 25
                accumulator = 0
                longest_chain = 0
            i += 1
        if longest_chain > 3:
            score += (longest_chain - 3) * 25 * accumulator

        # up right
        accumulator = 0
        longest_chain = 0
        i = 0
        # while _check_valid_indices(pt[0] + i, pt[1] + i):
        while (0 <= pt[0] - i) and (pt[1] + i < len(state[0])):
            if (state[pt[0] - i][pt[1] + i] == player_piece) or (state[pt[0] - i][pt[1] + i] == 0):
                if state[pt[0] - i][pt[1] + i] == player_piece:
                    accumulator += 1
                # accumulator += 1
                longest_chain += 1
            else:
                if longest_chain > 3:
                    score += (longest_chain - 3) * 25 * accumulator
                # score += (longest_chain - 3) * 100 - (longest_chain - accumulator) * 25
                accumulator = 0
                longest_chain = 0
            i += 1
        if longest_chain > 3:
            score += (longest_chain - 3) * 25 * accumulator

    return score


def calculate_heuristic(state: List[List[int]], computer_piece: int, human_piece: int) -> float:
    ai_rows = calc_row(state, computer_piece)
    ai_cols = calc_col(state, computer_piece)
    ai_diagonal = calc_diagonal(state, computer_piece)

    player_rows = calc_row(state, human_piece)
    player_cols = calc_col(state, human_piece)
    player_diagonal = calc_diagonal(state, human_piece)

    heuristic = ai_rows + ai_diagonal + ai_cols - player_rows - player_cols - player_diagonal
    return heuristic


state_ = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1]
]

r = calculate_heuristic(state_, 1, 2)
print("r = ", r)
