import random


def NumberGuesser():
    rando = random.randint(0, 100)
    guess = -1
    while guess != rando:
        guess = int(input("Type in a any number from 0 to 100."))
        if rando > guess >= 0:
            print("{} is too low!".format(guess))
        elif rando < guess <= 100:
            print("{} is too high!".format(guess))
        elif guess == rando:
            print("{} is correct!".format(guess))
        else:
            print("{} is an invalid guess. Please try again.".format(guess))


NumberGuesser()
