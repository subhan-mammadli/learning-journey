import csv
from tabulate import tabulate
from sys import argv, exit


def main():
    check_arguments()
    table = []
    filename = argv[1]

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for pizza, small, large in reader:
                table.append([pizza, small, large])
    except FileNotFoundError:
        exit("File does not exist")

    print(tabulate(table, headers="firstrow", tablefmt="grid"))


def check_arguments():
    if len(argv) == 1:
        exit("Too few command-line arguments")
    if len(argv) > 2:
        exit("Too many command-line arguments")

    if not argv[1].endswith(".csv"):
        exit("Not a CSV file")


if __name__ == "__main__":
    main()
