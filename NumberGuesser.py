import random


def NumberGuesser():
    rand = random.randint(0, 100)
    guess = -1
    while guess != rand:
        guess = int(input("Type in a any number from 0 to 100."))
        if rand > guess >= 0:
            print("{} is too low!".format(guess))
        elif rand < guess <= 100:
            print("{} is too high!".format(guess))
        elif guess == rand:
            print("{} is correct!".format(guess))
        else:
            print("{} is an invalid guess. Please try again.".format(guess))


NumberGuesser()
