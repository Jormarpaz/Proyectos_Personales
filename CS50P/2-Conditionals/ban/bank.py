def main():
    greeting = str(input())

    match greeting:
        case "hello":
            print("$0")
        case "h" == greeting[0]:
            print("$20")
        case _:
            print("$100")



main()
