def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    try:
        for v in vowels:
            word = word.replace(v, '')
        return word
    except (TypeError, AttributeError):
        return None

if __name__ == "__main__":
    main()
