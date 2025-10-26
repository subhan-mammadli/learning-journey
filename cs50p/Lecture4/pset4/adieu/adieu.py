import inflect

p = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    goodbye = p.join(names)
    print(f"Adieu, adieu, to {goodbye}")

main()
