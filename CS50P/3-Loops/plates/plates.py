def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check the length of the plate
    if not (2 <= len(s) <= 6):
        return False

    # Check if the plate starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters and position of numbers
    number_started = False
    for i in range(len(s)):
        if not s[i].isalnum():
            return False
        if s[i].isdigit():
            # The first number used cannot be '0'
            if s[i] == '0' and not number_started:
                return False
            number_started = True
        if number_started and s[i].isalpha():
            return False

    return True



main()
