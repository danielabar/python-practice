def make_guess(low, high):
    total = sum([low, high])
    return int(total / 2)


def get_guess(guess):
    return input("Is your number {}? Answer y(es) / l(ow) / h(igh)? ".format(guess))


def guess_game():
    answer = 'y'
    guess_count = 1
    low = 1
    high = 100
    guess = make_guess(1, 100)

    input("Pick a number between 1 and 100 inclusive but do not type it in. Hit enter to continue...")
    answer = get_guess(guess)

    while answer != 'y':
        guess_count += 1
        if answer == 'l':
            low = guess + 1
            guess = make_guess(guess + 1, high)
        if answer == 'h':
            high = guess - 1
            guess = make_guess(low, guess - 1)
        answer = get_guess(guess)

    print("Your number is {}, took {} guesses".format(str(guess), str(guess_count)))


if __name__ == '__main__':
    guess_game()
