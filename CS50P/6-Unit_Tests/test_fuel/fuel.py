def main():
    while True:
        try:
            frac = input("Fraction #/#: ")
            percentage = convert(frac)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    try:
        X, Y = fraction.split("/")
        X = int(X)
        Y = int(Y)

        if Y == 0:
            raise ZeroDivisionError

        if X > Y:
            raise ValueError

        percentage = (X / Y) * 100
        return percentage

    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()

