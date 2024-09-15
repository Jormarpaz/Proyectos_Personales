def main():

    d = {}
    key = 0

    while True:
        try:
            item = input().strip().upper()
            if item:
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1
        except (EOFError,KeyError):
            break

    for items in sorted(d):
            print(f"{d[items]} {items}")


main()
