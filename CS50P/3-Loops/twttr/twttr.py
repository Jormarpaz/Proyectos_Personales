def main():
    phrase = input("Input: ")

    vogals = ["A", "E", "I", "O", "U"]

    for char in phrase:
        if char.upper() in vogals:
            phrase = phrase.replace(char,"")

    print(f"Output: {phrase}")

main()
