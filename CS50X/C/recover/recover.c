#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    char *nombre = argv[1];
    FILE *card = fopen(nombre, "r");

    if (card == NULL)
    {
        printf("Image is empty\n");
        return 1;
    }

    BYTE buffer[512];
    int cantidad = 0;
    FILE *img = NULL;
    char filename[8];

    while (fread(buffer, sizeof(BYTE), 512, card) == 512)
    {
        // Check if buffer contains JPEG header
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // If a file is already open, close it
            if (img != NULL)
            {
                fclose(img);
            }

            // Create a new file and write to it
            sprintf(filename, "%03i.jpg", cantidad);
            img = fopen(filename, "w");
            cantidad++;
        }

        // If an image file is open, write the buffer to it
        if (img != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, img);
        }
    }

    // Close any remaining file
    if (img != NULL)
    {
        fclose(img);
    }

    fclose(card);
    return 0;
}
