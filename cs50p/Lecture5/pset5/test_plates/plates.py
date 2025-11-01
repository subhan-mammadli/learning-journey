def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    def starts_with_two_letters(s):
        return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()

    def valid_length(s):
        return 2 <= len(s) <= 6

    def numbers_at_the_end(s):
        number_started = False
        for c in s:
            if c.isdigit():
                number_started = True
            elif number_started == True and c.isalpha():
                return False
        return True

    def no_punctuation(s):
        return s.isalnum()

    def valid_first_number(s):
        for i in range(2, len(s)):
            if s[i].isdigit():
                if s[i] == '0':
                    return False
                break

        return True

    isvalid = {
        "starts_with_two_letters": starts_with_two_letters(s),
        "valid_length": valid_length(s),
        "numbers_at_the_end": numbers_at_the_end(s),
        "no_punctuation": no_punctuation(s),
        "valid_first_number": valid_first_number(s)
    }

    return (isvalid["starts_with_two_letters"] == True
            and isvalid["valid_length"] == True
            and isvalid["numbers_at_the_end"] == True
            and isvalid["no_punctuation"] == True
            and isvalid["valid_first_number"] == True
            )


if __name__ == "__main__":
    main()
