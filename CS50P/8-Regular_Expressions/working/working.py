import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Usamos una expresión regular para capturar el formato de tiempo esperado
    pattern = r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    # Capturamos las partes del tiempo
    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Si no hay minutos en el string, los ponemos como '00'
    if not start_minute:
        start_minute = "00"
    if not end_minute:
        end_minute = "00"

    # Convertimos a formato 24 horas
    start_time_24 = convert_to_24h(start_hour, start_minute, start_period)
    end_time_24 = convert_to_24h(end_hour, end_minute, end_period)

    return f"{start_time_24} to {end_time_24}"

def convert_to_24h(hour, minute, period):
    hour = int(hour)
    minute = int(minute)  # Asegurarse de que los minutos se conviertan a entero

    # Validamos que la hora sea válida en formato de 12 horas
    if hour < 1 or hour > 12:
        raise ValueError("Invalid hour")

    # Validamos que los minutos sean válidos
    if minute < 0 or minute > 59:
        raise ValueError("Invalid minute")

    # Convertimos la hora a formato de 24 horas según AM o PM
    if period == "AM":
        if hour == 12:
            hour = 0  # 12:00 AM es 00:00
    elif period == "PM":
        if hour != 12:
            hour += 12  # Para PM sumamos 12 excepto en el caso de 12 PM

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()
