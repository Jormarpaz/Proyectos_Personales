#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int x = 0; x < height; x++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            int ave =
                round((image[x][j].rgbtRed + image[x][j].rgbtGreen + image[x][j].rgbtBlue) / 3.0);

            // Update pixel values
            image[x][j].rgbtRed = ave;
            image[x][j].rgbtGreen = ave;
            image[x][j].rgbtBlue = ave;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int x = 0; x < height; x++)
    {
        for (int j = 0; j < width; j++)
        {
            // Compute sepia values
            int sepiaRed = round(.393 * image[x][j].rgbtRed + .769 * image[x][j].rgbtGreen +
                                 .189 * image[x][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[x][j].rgbtRed + .686 * image[x][j].rgbtGreen +
                                   .168 * image[x][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[x][j].rgbtRed + .534 * image[x][j].rgbtGreen +
                                  .131 * image[x][j].rgbtBlue);

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            else if (sepiaRed < 0)
            {
                sepiaRed = 0;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            else if (sepiaGreen < 0)
            {
                sepiaGreen = 0;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            else if (sepiaBlue < 0)
            {
                sepiaBlue = 0;
            }

            // Update pixel with sepia values
            image[x][j].rgbtRed = sepiaRed;
            image[x][j].rgbtGreen = sepiaGreen;
            image[x][j].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Loop over every pixel in the original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Initialize sums for each color channel
            int sumRed = 0, sumGreen = 0, sumBlue = 0;
            int count = 0;

            // Loop over the 3x3 box
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Check if neighboring pixel is within the image boundaries
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        sumRed += copy[ni][nj].rgbtRed;
                        sumGreen += copy[ni][nj].rgbtGreen;
                        sumBlue += copy[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            // Calculate the average color values
            image[i][j].rgbtRed = round((float) sumRed / count);
            image[i][j].rgbtGreen = round((float) sumGreen / count);
            image[i][j].rgbtBlue = round((float) sumBlue / count);
        }
    }
}
