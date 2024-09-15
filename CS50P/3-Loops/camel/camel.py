def main():
    phrase = input ("camelCase: ")

    for char in phrase:
        if char.isupper():
            phrase = phrase.replace(char,"_" + char.lower())

    print("snake_case:", phrase)


main()
