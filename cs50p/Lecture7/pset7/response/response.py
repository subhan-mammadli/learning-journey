import validators


def main():
    print(check(input("What's your email address? ")))


def check(s):
    if validators.email(s):
        return "Valid"
    return "Invalid"


if __name__ == "__main__":
    main()
