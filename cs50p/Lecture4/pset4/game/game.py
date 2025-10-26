import random


def main():
    n = get_positive("Level: ")
    number = random.randint(1, n)

    while True:
        guess = get_positive("Guess: ")

        if guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break


def get_positive(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


main()
