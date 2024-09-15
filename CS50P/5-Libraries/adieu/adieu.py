import sys
import inflect

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input().strip()
            if name:
                names.append(name)
        except EOFError:
            break

    adieu_message = format_adieu(names, p)
    print(adieu_message)

def format_adieu(names, inflect_engine):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        # Ensure the use of Oxford comma with correct formatting
        formatted_names = inflect_engine.join(names)
        return f"Adieu, adieu, to {formatted_names}"

if __name__ == "__main__":
    main()
