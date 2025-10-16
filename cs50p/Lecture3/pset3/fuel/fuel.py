def main():
    fraction = get_fraction()
    if int(fraction) <= 1:
        print("E")
    elif int(fraction) >= 99:
        print("F")
    else:
        print(fraction + "%")

def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split('/')
            x, y = int(x), int(y)
            if x > y or y <= 0 or x < 0:
                continue
            else:
                return f"{x * 100 / y:.0f}"
        except ValueError:
            pass

main()
