def main():
    d = {}

    while True:
        try:
            item = input().upper().strip()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except EOFError:
            d = dict(sorted(d.items()))
            for item in d:
                print(d[item], item)
            break

main()
