#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    float letras = 0.0;
    float frases = 0.0;
    float palabras = 1.0;
    float L, S;
    int index;
    string texto = get_string("Text: ");

    for (int x = 0; x < strlen(texto); x++)
    {
        if (texto[x] != ' ' && isalpha(texto[x]))
        {
            letras++;
        }
        else if ((texto[x] == '.' || texto[x] == '?' || texto[x] == '!') &&
                 (isspace(texto[x + 1]) || ispunct(texto[x + 1]) || x == strlen(texto) - 1))
        {
            frases++;
        }
        else if (isspace(texto[x]) || x == strlen(texto) - 1)
        {
            palabras++;
        }
    }

    L = (letras * 100) / palabras;
    S = (frases * 100) / palabras;

    index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
