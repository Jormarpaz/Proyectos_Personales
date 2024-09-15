import validators

def main():
    email = input("What's your email address? ")

    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

def validate_email(email):
    # Utilizamos la función validators.email para validar el correo electrónico
    return validators.email(email)

if __name__ == "__main__":
    main()
