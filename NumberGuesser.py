import random


def NumberGuesser():
    randomi = random.randint(0, 100)
    guess = -1
    while guess != randomi:
        guess = int(input("Type in a any number from 0 to 100."))
        if randomi > guess >= 0:
            print("{} is too low!".format(guess))
        elif randomi < guess <= 100:
            print("{} is too high!".format(guess))
        elif guess == randomi:
            print("{} is correct!".format(guess))
        else:
            print("{} is an invalid guess. Please try againn.".format(guess))


NumberGuesser()
