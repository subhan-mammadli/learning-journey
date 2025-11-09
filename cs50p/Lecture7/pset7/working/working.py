import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'((?:[1-9]|1[0-2])(?::[0-5]\d)? (?:AM|PM)) to ((?:[1-9]|1[0-2])(?::[0-5]\d)? (?:AM|PM))'
    if matches := re.search(pattern, s):
        captured = lambda i: matches.group(i).split(" ")
        get_type = lambda i: captured(i)[1]
        get_time = lambda i: captured(i)[0]

        def convert_format(i):
            time = get_time(i).split(":")
            hour = int(time[0])
            minute = time[1] if len(time) > 1 else "00"
            if get_type(i) == 'PM' and hour != 12:
                hour += 12
            elif get_type(i) == 'AM' and hour == 12:
                hour = 0

            return f"{hour:02d}:{minute}"

        return f"{convert_format(1)} to {convert_format(2)}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
