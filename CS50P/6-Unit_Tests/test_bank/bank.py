def main():
    print(value(str(input())))


def value(greeting):

    match greeting:
        case "hello":
            print("$0")
            return 0
        case "h" == greeting[0]:
            print("$20")
            return 20
        case _:
            print("$100")
            return 100


if __name__ == "__main__":
    main()
