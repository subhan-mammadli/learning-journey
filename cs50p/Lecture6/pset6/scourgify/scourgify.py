import csv

from sys import argv, exit


def main():
    check_arguments() 
    try:
        with open(argv[1]) as beforefile:
            reader = csv.DictReader(beforefile)
            with open(argv[2], 'w') as afterfile:
                writer = csv.DictWriter(afterfile, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(',')
                    first = first.strip()
                    house = row["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        exit("Could not read invalid_file.csv")


def check_arguments():
    if len(argv) == 1:
        exit("Too few command-line arguments")
    if len(argv) > 3:
        exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
