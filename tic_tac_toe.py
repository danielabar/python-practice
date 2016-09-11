#!/usr/bin/env python
"""Generate a tic tac toe board.

Usage:

    python tic_tac_toe.py <size>

"""
import sys


def is_player(token):
    return token in [1, 2]


# >>> import importlib
# >>> importlib.reload(tic_tac_toe)
# board = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
# board_2_won = [[2, 2, 2], [2, 1, 0], [2, 1, 1]]
def who_won(board):
    # assume nobody won
    winner = 0

    # check rows
    for row in board:
        unique_vals = set(row)
        candidate = unique_vals.pop()
        if (len(unique_vals) == 0 and is_player(candidate)):
            winner = candidate

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
