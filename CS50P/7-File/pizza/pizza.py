import csv,sys,os

from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py pizza.csv")

    pizza = sys.argv[1]

    if not pizza.endswith(".csv"):
        sys.exit("Error: The file must have a .csv extension")

    if not os.path.isfile(pizza):
        sys.exit(f"Error: File '{pizza}' does not exist ")

    try:
        with open(pizza) as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = [row for row in reader]

        # Use tabulate to format the table as ASCII art
        print(tabulate(rows, headers, tablefmt="grid"))

    except Exception as e:
        sys.exit(f"Error: Could not read the file. {e}")


if __name__ == "__main__":
    main()

