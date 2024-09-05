#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int amount, operacion1, operacion2, operacion3, operacion4, resultado;

    do
    {
        amount = get_int("Amount greater than 0: ");
    }
    while (amount <= 0);

    printf("Change owned : %i\n", amount);
    operacion1 = amount / 25;
    amount = amount - 25 * operacion1;
    operacion2 = amount / 10;
    amount = amount - 10 * operacion2;
    operacion3 = amount / 5;
    amount = amount - 5 * operacion3;
    operacion4 = amount / 1;
    amount = amount - 1 * operacion4;
    resultado = operacion1 + operacion2 + operacion3 + operacion4;
    printf("Change:%i\n", resultado);
}
