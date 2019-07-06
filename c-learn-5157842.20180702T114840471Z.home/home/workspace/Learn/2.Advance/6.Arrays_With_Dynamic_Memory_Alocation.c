#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int n = 5; //Length of Array, used to set later
    char *pvowels = (char *) malloc(n * sizeof(char)); //Dynamically allocates the length of memory used for pvowels, length is n * length needed for a char
    //(char *) is not needed and is pretty much irrelevant 
    int i;

    pvowels[0] = 'A'; //Both Methods can be used to assign values
    pvowels[1] = 'E';
    pvowels[2] = 'O';
    *(pvowels + 3) = 'I';
    *(pvowels + 4) = 'U';

    for (i = 0; i < n; i++) 
    {
        printf("%c ", pvowels[i]);
    }

    printf("\n");

    free(pvowels); //BE RESPONSIBLE free memory used in pvowels when you are done using it
}