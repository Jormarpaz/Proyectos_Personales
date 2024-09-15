def main():

    print(shorten(input("Input: ")))


def shorten(word):

    vogals = ["A", "E", "I", "O", "U"]

    for char in word:
        if char.upper() in vogals:
            word = word.replace(char,"")

    return word


if __name__ == "__main__":
    main()
