#!/usr/bin/env python
"""Generate a tic tac toe board.

Usage:

    python tic_tac_toe.py <size>

"""
import sys


NO_PLAYER = 0
FIRST_PLAYER = 1
SECOND_PLAYER = 2


def is_nobody(token):
    return token == NO_PLAYER


def is_player(token):
    return token in [FIRST_PLAYER, SECOND_PLAYER]


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
        row = [NO_PLAYER] * board_size
        board.append(row)
    return board


def convert_move(str_val):
    return int(str_val) - 1


def translate_move(move):
    parsed = move.split(",")
    return list(map(convert_move, parsed))


def update_board(board, move, player):
    board[move[0]][move[1]] = player


def validate(move):
    result = (true, "valid")
    return result


def play(board):
    num_moves = 0
    move = None

    while (move != "quit"):
        whose_turn = FIRST_PLAYER if (num_moves % 2 == 0) else SECOND_PLAYER
        print("Player {}: Enter move in row,col format, for example: 1,2. Type quit to exit.".format(whose_turn))
        move = input()
        if (move != "quit"):
            translated_move = translate_move(move)
            update_board(board, translated_move, whose_turn)
            render_board(len(board), board)
            num_moves += 1


def main(size):
    board_size = int(size)
    board = generate_board(board_size)
    render_board(board_size, board)
    play(board)


if __name__ == '__main__':
    main(sys.argv[1])
