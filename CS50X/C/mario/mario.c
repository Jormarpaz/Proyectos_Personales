#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int number=0;
    do{
     number = get_int("¿How tall do u want it?\n");
    } while (number<=0);


    for(int fila = 0; fila<number;fila++){
        for(int columna = 0;columna<number-fila-1;columna++){
            printf(" ");
        }
        for(int columna=0;columna<=fila;columna++){
            printf("#");
        }
        printf("  ");
        for(int columna = 0;columna<=fila;columna++){
            printf("#");
        }
        printf("\n");
    }
}



/* Esto permite hacer la piramide hacia la derecha
for(int fila = 0;fila<=number;fila++){
        for(int columna = fila;columna>=1;columna--){
            printf("#");
        }
        printf("\n");
    }
*/
