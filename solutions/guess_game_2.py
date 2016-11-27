import sys
import logging

MIN = 1
MAX = 100


def make_guess(low, high):
    total = sum([low, high])
    return int(total / 2)


def get_guess(guess):
    return input("Is your number {}? Answer y(es) / l(ow) / h(igh) / q(uit)? ".format(guess))


def guess_game():
    answer = 'y'
    guess_count = 1
    low = MIN
    high = MAX
    guess = make_guess(low, high)

    input("Pick a number between 1 and 100 inclusive but do not type it in. Hit enter to continue...")
    previous_answer = -1
    answer = get_guess(guess)

    while answer != 'y':
        if answer == 'q':
            sys.exit()

        logging.debug("low = {}, high = {}, guess = {}".format(low, high, guess))

        if low > MAX or high < MIN:
            print("Sorry, this isn't working out. Goodbye.")
            sys.exit()

        guess_count += 1
        if answer == 'l':
            low = guess + 1
            guess = make_guess(low, high)
        if answer == 'h':
            high = guess - 1
            guess = make_guess(low, high)
        answer = get_guess(guess)

    print("Your number is {}, took {} guesses".format(str(guess), str(guess_count)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    guess_game()
