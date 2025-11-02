from sys import argv, exit
from PIL import Image, ImageOps


def main():
    check_arguments()
    try:
        image = Image.open(argv[1])
    except FileNotFoundError:
        exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = ImageOps.fit(image, size)
    image.paste(shirt, (0, 0), shirt)
    image.save(argv[2])


def check_arguments():
    if len(argv) == 1:
        exit("Too few command-line arguments")
    elif len(argv) != 3:
        exit("Too many command-line arguments")

    extensions = ['png', 'jpg', 'jpeg']
    find_extension = lambda file: file.split('.')[1]

    if find_extension(argv[1]) not in extensions or find_extension(argv[2]) not in extensions:
        exit("Invalid output")
    elif find_extension(argv[1]) != find_extension(argv[2]):
        exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
