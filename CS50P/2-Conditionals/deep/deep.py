def main():
    answer = input("Answer to the Great Question of Life: ")
    answer = answer.replace(" ","").lower()

    match answer:
        case "42" | "forty-two" | "fortytwo" :
            print("Yes")
        case _:
            print("No")



main()
