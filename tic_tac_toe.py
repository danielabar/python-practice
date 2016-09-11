#!/usr/bin/env python
"""Generate a tic tac toe board.

Usage:

    python tic_tac_toe.py <size>

"""
import sys


def is_nobody(token):
    return token == 0


def is_player(token):
    return token in [1, 2]


def check_rows(board):
    # assume nobody won
    winner = 0

    for row in board:
        unique_vals = set(row)
        candidate = unique_vals.pop()
        if (len(unique_vals) == 0 and is_player(candidate)):
            winner = candidate
            break

    return winner


# >>> import importlib
# >>> importlib.reload(tic_tac_toe)
# winner_is_1_horizontal = [[1, 1, 1], [2, 1, 0], [0, 0, 2]]
# winner_is_2_vertical = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
# winner_is_1_vertical = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
# winner_is_1_diagonal = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
# no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
def who_won(board):
    winner = check_rows(board)

    if (is_nobody(winner)):
        # assumes same number of rows and cols
        transpose = map(list, zip(*board))
        winner = check_rows(transpose)

    return winner


def generate_vertical(board_size):
    bar = ["|"] * (board_size + 1)
    bar_with_spaces = "   ".join(bar)
    return bar_with_spaces


def generate_horizontal(board_size):
    bars = ["---"] * (board_size)
    bars_with_spaces = " ".join(bars)
    return " " + bars_with_spaces + " "


def generate_board(board_size):
    for i in range(board_size+1):
        print(generate_horizontal(board_size))
        if (i < board_size):
            print(generate_vertical(board_size))


def main(size):
    board_size = int(size)
    generate_board(board_size)


if __name__ == '__main__':
    main(sys.argv[1])
