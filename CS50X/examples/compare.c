#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

    string s = get_string("s: ");
    string t = get_string("t: ");

    //int i = get_int("i: ");
    //int j = get_int("j: ");

    //Recordemos que una string al final es char *, entonces cuando igualamos dos string para compararlas, en realidad estamos
    //comparando sus direcciones de memoria, no su contenido, porque su contenido, tecnicamente, es la direccion del primer
    //elemento de la cadena

    //Strcmp devuelve 0 si son iguales, y 1 si no lo son

    if(strcmp(s,t) == 0)
    {
        printf("Same\n");
        printf("%p\n", s);
        printf("%p\n", t);
    }
    else
    {
        printf("Different\n");
    }
}
