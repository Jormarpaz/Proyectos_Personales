#import <stdio.h>
#import <string.h>
#import <ctype.h>
#import <cs50.h>
#import <stdlib.h>

bool solo_n(string s);
string rotation(string s,int i);

int main(int argc, string argv[])
{
    if( argc == 2 ) {
        if(solo_n(argv[argc-1]))
        {
            printf("plaintext:  ");
            string s = get_string("");
            printf("ciphertext: ");
            printf("%s\n",rotation(s,atoi(argv[1])));
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
   }
   else if( argc > 2 ) {
        printf("Usage: ./caesar key\n");
      return 1;
   }
   else {
        printf("Usage: ./caesar key\n");
      return 1;
   }
}

bool solo_n(string s)
{
    for(int x = 0; x < strlen(s); x++)
    {
        if (!isdigit(s[x])){
            return false;
        }
    }
    return true;
}

string rotation(string s,int i)
{
    int n = strlen(s);
    char *j = malloc(n+1);

    if(j == NULL){
        printf("Memory allocation error\n");
        exit(1);
    }

    for (int x = 0; x < n; x++) {
        if (isupper(s[x])) {
            j[x] = ((s[x] - 'A' + i) % 26) + 'A'; // Para mayúsculas
        } else if (islower(s[x])) {
            j[x] = ((s[x] - 'a' + i) % 26) + 'a'; // Para minúsculas
        } else {
            j[x] = s[x]; // Dejar sin cambios los caracteres no alfabéticos
        }
    }

    // Asegurarse de que la nueva cadena está terminada en null
    j[n] = '\0';

    return j;
}
