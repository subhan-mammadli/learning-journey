from random import randint


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for i in range(3):
            try:
                user_input = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            if user_input == answer:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return randint(0, 9)
        case 2:
            return randint(10, 99)
        case 3:
            return randint(100, 999)


if __name__ == "__main__":
    main()
