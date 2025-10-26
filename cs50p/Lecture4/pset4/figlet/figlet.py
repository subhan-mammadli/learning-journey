from pyfiglet import Figlet
from sys import exit, argv
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

def get_font():
    if len(argv) == 1:
        return choice(fonts)
    elif argv[1] in ("-f", "--font"):
        if argv[2] in fonts:
            return argv[2]
        exit("Invalid usage")
    exit("Invalid usage")

def main():
    font = get_font()
    text = input("Input: ")
    figlet.setFont(font=font)
    print(figlet.renderText(text))


main()
