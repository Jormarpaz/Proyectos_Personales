from cs50 import get_float

while True:
    cambio = get_float("Cambio: ")
    try:
        if cambio > 0.00:
            break
        else:
            print("Not valid")
    except ValueError:
        print("Not valid")

cambio *= 100

operacion1 = cambio // 25
cambio = cambio % 25
operacion2 = cambio // 10
cambio = cambio % 10
operacion3 = cambio // 5
cambio = cambio % 5
operacion4 = cambio // 1
print(f"Resultado : {operacion1 + operacion2 + operacion3 + operacion4}")
