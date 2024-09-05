// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 100;

// Hash table
node *table[N];

int contador = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Obtener el valor hash de la palabra
    unsigned int hash_value = hash(word);

    // Buscar en la lista enlazada en el índice de la tabla hash
    node *cursor = table[hash_value];
    while (cursor != NULL)
    {
        // Comparar las palabras sin distinguir mayúsculas y minúsculas
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    // Si no se encuentra la palabra, devolver false
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hash_value = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hash_value = (hash_value * 31 + tolower(word[i])) % N;
    }
    return hash_value;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    char word[LENGTH + 1]; // Reservamos espacio para la palabra

    while (fscanf(input, "%s", word) !=
           EOF) // Modificamos la condición de bucle para verificar el final del archivo
    {
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(input);
            return false;
        }
        strcpy(new_node->word, word);

        unsigned int n = hash(word);
        new_node->next = table[n];
        table[n] = new_node;

        contador++; // Incrementamos el contador de palabras
    }

    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return contador;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
