def main():

    while True:
        try:
            frac = input("Fraction #/#:")
            X,Y = frac.split("/")
            X = int(X)
            Y = int(Y)

            if Y == 0 :
                raise ZeroDivisionError

            if X > Y :
                raise ValueError

            percentage = (X / Y) * 100

            if percentage <= 1 :
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")

            break

        except (ValueError, ZeroDivisionError):
            continue



main()
