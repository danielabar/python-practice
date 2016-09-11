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


def build_diagonals(board):
    diagonals = []
    size = len(board)

    # left to right
    left_to_right = []
    for row_idx, row in enumerate(board):
        for col_idx, col in enumerate(row):
            if (row_idx == col_idx):
                left_to_right.append(col)
    diagonals.append(left_to_right)

    # right to left
    right_to_left = []
    for row_idx, row in enumerate(board):
        for col_idx, col in reversed(list(enumerate(row))):
            if (row_idx == (size - col_idx - 1)):
                right_to_left.append(col)
    diagonals.append(right_to_left)

    return diagonals


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


def who_won(board):
    winner = check_rows(board)

    if (is_nobody(winner)):
        # assumes same number of rows and cols
        transpose = map(list, zip(*board))
        winner = check_rows(transpose)

        if (is_nobody(winner)):
            diagonals = build_diagonals(board)
            winner = check_rows(diagonals)

    return winner


def generate_vertical(board_size, row):
    output = []
    for val in row:
        output.append("|")
        output.append(" ")
        output.append(str(val))
        output.append(" ")
    return "".join(output) + "|"


def generate_horizontal(board_size):
    bars = ["---"] * (board_size)
    bars_with_spaces = " ".join(bars)
    return " " + bars_with_spaces + " "


def render_board(board_size, board):
    for i in range(board_size+1):
        print(generate_horizontal(board_size))
        if (i < board_size):
            print(generate_vertical(board_size, board[i]))


def generate_board(board_size):
    board = []
    for i in range(board_size):
        row = [0] * board_size
        board.append(row)
    return board


def main(size):
    board_size = int(size)
    board = generate_board(board_size)
    render_board(board_size, board)


if __name__ == '__main__':
    main(sys.argv[1])
