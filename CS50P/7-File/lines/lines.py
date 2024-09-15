import sys, os


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]


    if not filename.endswith(".py"):
        sys.exit("Error: The file must have a .py extension")

    if not os.path.isfile(filename):
        sys.exit(f"Error: File '{filename}' does not exist ")

    loc = count_lines_of_code(filename)
    print(loc)

def count_lines_of_code(filename):
    try:
        with open(filename) as file:
            lines = file.readlines()

        code_lines = 0

        for line in lines:
            new_line = line.strip()

            if new_line and not new_line.startswith("#"):
                code_lines += 1

        return code_lines

    except FileNotFoundError:
        sys.exit(f"Error:_File '{filename}' not found")




if __name__ == "__main__":
    main()



