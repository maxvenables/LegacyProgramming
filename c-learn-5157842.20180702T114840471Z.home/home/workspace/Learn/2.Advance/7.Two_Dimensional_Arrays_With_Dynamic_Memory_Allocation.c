#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main()
{
    int nrows = 2; //numeber of rows and collumns to be used later
    int ncols = 5;
    
    char **pvowels = (char **) malloc(nrows * sizeof(char *)); //Creates pointer that points to multidimensional array of nrows
    //** used to signify multidimesionality
    
    for(int i = 0; i < nrows; i++)
    {
        pvowels[i] = (char *) malloc(ncols * sizeof(char));//creates arrays in multidimensional array of length ncols
    }
    
    pvowels[0][0] = 'A';
    pvowels[0][1] = 'E';
    pvowels[0][2] = 'I';
    pvowels[0][3] = 'O';
    pvowels[0][4] = 'U';

    pvowels[1][0] = 'a';
    pvowels[1][1] = 'e';
    pvowels[1][2] = 'i';
    pvowels[1][3] = 'o';
    pvowels[1][4] = 'u';
    
    for (int i = 0; i < nrows; i++) 
    {
        for(int j = 0; j < ncols; j++) 
        {
            printf("%c ", pvowels[i][j]);
        }
    printf("\n");
    }
    
}