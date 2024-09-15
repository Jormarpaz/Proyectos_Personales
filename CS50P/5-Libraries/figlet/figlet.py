from pyfiglet import Figlet
import random
import sys

def main():
    f = Figlet()

    if len(sys.argv) not in [1, 3]:
        sys.exit("Usage: python script.py [-f | --font <fontname>]")
    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Usage: python script.py [-f | --font <fontname>]")
        elif sys.argv[2] not in f.getFonts():
            sys.exit("Usage: python script.py [-f | --font <fontname>]")

    str = input("Input: ")

    if len(sys.argv) == 1:
        f.setFont(font=random.choice(f.getFonts()))
    elif len(sys.argv) == 3:
        f.setFont(font=sys.argv[2])

    print(f"Output: {f.renderText(str)}")



main()
