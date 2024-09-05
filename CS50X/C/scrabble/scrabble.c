#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string player[2];
    int sum[2] = {0};
    char characters[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    int amount[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    for (int x = 0; x < 2; x++)
    {
        player[x] = get_string("Word: ");
        for (int j = 0; j < strlen(player[x]); j++)
        {
            player[x][j] = toupper(player[x][j]);
            for (int y = 0; y < 26; y++)
            {
                if (player[x][j] == characters[y])
                {
                    sum[x] = sum[x] + amount[y];
                }
            }
        }
    }

    if (sum[0] == sum[1])
    {
        printf("Tie!\n");
    }
    else if (sum[0] > sum[1])
    {
        printf("Player 1 wins!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }
}
