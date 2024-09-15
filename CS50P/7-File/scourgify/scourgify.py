import csv,sys,os


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input = sys.argv[1]
    output = sys.argv[2]

    if not input.endswith(".csv"):
        sys.exit("Error: The input file must have a .csv extension")

    if not output.endswith(".csv"):
        sys.exit("Error: The output file must have a .csv extension")

    if not os.path.isfile(input):
        sys.exit(f"Error: File '{input}' does not exist ")

    try:
        with open(input, mode = "r") as file:
            reader = csv.DictReader(file)
            students = []

            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                students.append({"first": first, "last": last, "house": house})

        with open(output, mode = "w", newline = "") as file:
            writer = csv.DictWriter(file,fieldnames = ["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except Exception as e:
        sys.exit(f"Error: Could not read the file. {e}")


if __name__ == "__main__":
    main()
