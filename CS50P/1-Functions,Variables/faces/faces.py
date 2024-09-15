def main():
    prompt = input()
    print(convert(prompt))


def convert(prompt):
    return str(prompt).replace(":)","🙂").replace(":(","🙁")


main()
