from emoji import emojize

def main():
    emoji = input("Input: ")
    output = emojize(emoji, language='alias')
    print(f"Output: {output}")

main()
