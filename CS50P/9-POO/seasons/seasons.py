from datetime import date
import inflect
import sys


def main():
    birthdate_str = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birthdate = date.fromisoformat(birthdate_str)
    except ValueError:
        sys.exit("Invalid date format")

    today = date.today()
    minutes = calculate_minutes(birthdate, today)

    p = inflect.engine()
    minutes_in_words = p.number_to_words(minutes, andword="")

    print(f"{minutes_in_words.capitalize()} minutes")


def calculate_minutes(birthdate, today):
    difference = today - birthdate
    return round(difference.total_seconds() / 60)


if __name__ == "__main__":
    main()
