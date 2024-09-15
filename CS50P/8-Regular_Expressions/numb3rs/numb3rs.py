import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
# Usamos una expresión regular para verificar el formato
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.match(pattern, ip)

    if match:
        # Convertimos cada grupo a entero y verificamos que esté en el rango 0-255
        for part in match.groups():
            if not (0 <= int(part) <= 255):
                return False
        return True
    return False


if __name__ == "__main__":
    main()
