#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void){

    char cadena [25];

    long card = get_long("Number: ");
    sprintf(cadena,"%ld",card);

        if(cadena[0]==4 && ((strlen(cadena)>=13)&&(strlen(cadena)<=16))){
            printf("VISA\n");
        }else{
            printf("INVALID\n");
        }

}
