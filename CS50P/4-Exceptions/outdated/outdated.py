def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month_to_number = {month: str(index + 1).zfill(2) for index, month in enumerate(months)}

    while True:
        try:
            date_input = input("Date: ").strip()
            date_output = parse_date(date_input, month_to_number)
            if date_output:
                print(date_output)
                break
        except ValueError:
            continue

def parse_date(date_input, month_to_number):
    # Check for numeric date format (MM/DD/YYYY)
    if "/" in date_input:
        parts = date_input.split("/")
        if len(parts) == 3:
            month, day, year = parts
            if is_valid_date(year, month, day):
                return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"

    # Check for textual date format (Month DD, YYYY)
    if " " in date_input and "," in date_input:
        parts = date_input.split(" ")
        if len(parts) == 3:
            month_name = parts[0]
            day = parts[1].strip(",")
            year = parts[2]
            month = month_to_number.get(month_name)
            if month and is_valid_date(year, month, day):
                return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"

    return None

def is_valid_date(year, month, day):
    # Ensure day, month, and year are valid integers
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False
    day = int(day)
    month = int(month)
    year = int(year)

    # Check if the day and month are in valid range
    if 1 <= day <= 31 and 1 <= month <= 12:
        return True
    return False


main()
