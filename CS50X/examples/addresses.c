#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //printf("%p\n", &n);
    //Si el comando de print es %p y empleamos & estamos preguntando por la "ubicacion" en memoria de la variable, esto es lo que se conoce como
    //puntero.

    //int *p = &n;
    //printf("%p\n", p);
    //Si aplicamos lo anterior, y en este caso usamos * para definir una variable junto a &, le estamos diciendo al ordenador :
    //almacena en esta variable la ubicacion en memoria de esta otra variable

    //int *p = &n;
    //printf("%i\n", *p);
    //Haciendo este cambio, le pedimos al ordenador, oye, muestrame por pantalla el valor integer que "contiene" esta variable
    //el * al final es una forma de direccionar, address, y realmente hacen cosas distintas alla donde he declarado p y donde la muestro
    //pero funciona asi, dato curioso, los punteros ocupan mas en memoria que una variable p.e

    //string s = "HI!";
    //printf("%p\n",s);
    //printf("%p\n",&s[0]);
    //Con las string, al tener un character que especifica el final de la string, el puntero indica donde está el primer elemento de la
    //cadena, y sabe donde tiene que terminar de buscar

    //Al final, una String es un char *, indicando ese * que la variable es el address de una char, del primer char en la string
    //char *s = "HI!";

    char *s = "HI!";
    printf("%c\n",s[0]);

}
