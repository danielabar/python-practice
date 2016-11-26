#!/usr/bin/envn python

"""Pick a random word from text file.

Usage:

    python pick_word

"""
import random


def pick_word():
    with open('sowpods.txt', 'r') as sowpods:
        lines = sowpods.readlines()
        num_lines = len(lines)
        some_line_num = random.randint(0, num_lines - 1)
        print('Your random word is {}'.format(lines[some_line_num]))


if __name__ == '__main__':
    pick_word()
