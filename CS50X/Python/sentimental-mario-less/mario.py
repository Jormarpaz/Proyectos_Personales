

while True:
    bloques = input("Cuantos bloques de altura? ")

    try:
        bloques = int(bloques)
        if 1 <= bloques <= 8:
            break  # Salir del bucle si la conversión fue exitosa y está en el rango
        else:
            print("El número no está en el rango de 1 a 8. Inténtelo de nuevo.")
    except ValueError:
        print("Not valid, try again")

for linea in range(1, bloques+1):
    if bloques == 1:
        print("#")
        break
    for columnax in range(bloques-linea):
        print(" ", end="")

    for columnay in range(linea):
        print("#", end="")

    print()
