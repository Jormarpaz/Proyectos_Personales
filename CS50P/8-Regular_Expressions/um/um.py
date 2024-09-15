import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Usamos una expresión regular que busca "um" como palabra independiente, insensible a mayúsculas
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()
