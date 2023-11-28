from typing import List

from src.utilities.get_score import get_player_score


def check_three(state: List[List[int]], player_piece: int):
    three_count = 0
    ROW_COUNT = len(state)
    COL_COUNT = len(state[0])
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if c < COL_COUNT - 3:
                # check horizontal and empty to the right
                if state[r][c] == state[r][c + 1] == state[r][c + 2] == player_piece and state[r][c + 3] == 0:
                    three_count += 1

                if r < ROW_COUNT - 3:
                    # check diagonal and empty down
                    if state[r][c] == state[r + 1][c + 1] == state[r + 2][c + 2] == player_piece and state[r + 3][
                        c + 3] == 0:
                        three_count += 1

            elif c >= COL_COUNT - 3:
                # check horizontal and empty to the left
                if state[r][c] == state[r][c - 1] == state[r][c - 2] == player_piece and state[r][c - 3] == 0:
                    three_count += 1
                if r < ROW_COUNT - 3:
                    # check diagonal and empty up
                    if state[r][c] == state[r + 1][c - 1] == state[r + 2][c - 2] == player_piece and state[r + 3][
                        c - 3] == 0:
                        three_count += 1

            if r >= 3:
                if state[r][c] == state[r - 1][c] == state[r - 2][c] == player_piece and state[r - 3][c] == 0:
                    three_count += 1

    return three_count


def check_two(state: List[List[int]], player_piece: int):
    two_count = 0
    ROW_COUNT = len(state)
    COL_COUNT = len(state[0])
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            if c < COL_COUNT - 3:
                # check horizontal and empty to the right
                if state[r][c] == state[r][c + 1] == player_piece and state[r][c + 2] == state[r][c + 3] == 0:
                    two_count += 1

                if r < ROW_COUNT - 3:
                    # check diagonal and empty down
                    if state[r][c] == state[r + 1][c + 1] == player_piece and state[r + 2][c + 2] == state[r + 3][
                        c + 3] == 0:
                        two_count += 1

            elif c >= COL_COUNT - 3:
                # check horizontal and empty to the left
                if state[r][c] == state[r][c - 1] == player_piece and state[r][c - 2] == state[r][c - 3] == 0:
                    two_count += 1
                if r < ROW_COUNT - 3:
                    # check diagonal and empty up
                    if state[r][c] == state[r + 1][c - 1] == player_piece and state[r + 2][c - 2] == state[r + 3][
                        c - 3] == 0:
                        two_count += 1

            if r >= 2:
                if state[r][c] == state[r - 1][c] == player_piece and state[r - 2][c] == 0:
                    two_count += 1
    return two_count


def check_more_than_three(state: List[List[int]], player_piece: int):
    return get_player_score(state, player_piece)


def calculate_heuristic(state: List[List[int]], computer_piece: int, human_piece: int) -> float:
    three_ai_score = check_three(state, computer_piece)
    two_ai_score = check_two(state, computer_piece)
    more_than_three_ai_score = check_more_than_three(state, computer_piece)
    three_human_score = check_three(state, human_piece)
    two_human_score = check_two(state, human_piece)
    more_than_three_human_score = check_more_than_three(state, human_piece)
    # print("three_ai_score = ", three_ai_score, ", two_ai_score = ", two_ai_score, ", more_than_three_ai_score = ",more_than_three_ai_score)
    # print("three_human_score = ", three_human_score, ", two_human_score = ", two_human_score, ", more_than_three_human_score = ",more_than_three_human_score)

    heuristic = float(100 * more_than_three_ai_score + 75 * three_ai_score + 50 * two_ai_score - (
            100 * more_than_three_human_score + 75 * three_human_score + 50 * two_human_score))

    return heuristic

# state = [
#     [1, 0, 0, 0, 0, 0, 2],
#     [1, 1, 1, 0, 0, 0, 2],
#     [0, 1, 2, 2, 2, 0, 2],
#     [0, 1, 1, 0, 2, 2, 2],
#     [1, 1, 1, 1, 1, 1, 2],
#     [1, 1, 2, 2, 1, 2, 2]
# ]
#
# r = calculate_heuristic(state, 1, 2)
# print("r = ", r)
