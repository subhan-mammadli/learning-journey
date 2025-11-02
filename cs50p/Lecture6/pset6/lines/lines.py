from sys import argv, exit


def main():
    code = read_file()
    count = 0
    for line in code:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        count += 1
    print(count)


def read_file():
    if len(argv) == 1:
        exit("Too few command-line arguments")
    if len(argv) > 2:
        exit("Too many command-line arguments")

    filename = argv[1]

    if not filename.endswith(".py"):
        exit("Not a Python file")

    try:
        with open(filename) as file:
            return file.readlines()
    except FileNotFoundError:
        exit("File does not exist")


if __name__ == "__main__":
    main()
