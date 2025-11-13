from datetime import date, datetime
import inflect
import sys


def main():
    print(calculate(input("Date of Birth: ")))


def calculate(birthday):
    p = inflect.engine()
    try:
        birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    days = today - birthday
    minutes = int(days.days) * 24 * 60
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
