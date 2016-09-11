#!/usr/bin/env python
"""Generate a tic tac toe board.

Usage:

    python tic_tac_toe.py <size>

"""
import sys


def generate_horizontal(board_size):
    a = ["--"] * 4
    return " ".join(a)


def generate_board(board_size):
    for i in range(board_size):
        print(generate_horizontal(board_size))


def main(size):
    board_size = int(size)
    generate_board(board_size)


if __name__ == '__main__':
    main(sys.argv[1])
