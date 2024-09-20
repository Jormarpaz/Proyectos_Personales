def main():
    # Solicitamos el saludo del usuario y quitamos los espacios sobrantes
    greeting = input("Greeting: ").strip().lower()

    # Verificamos las condiciones
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
