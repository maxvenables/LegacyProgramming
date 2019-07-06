#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char vowels[] = {"A", "E", "I", "O", "U"};
    char *pvowels = &vowels; //pointer can be made of array just as any other data type
    
    // Print the addresses
    for (i = 0; i < 5; i++) 
    {
        printf("&vowels[%d]: %u, pvowels + %d: %u, vowels + %d: %u\n", i, &vowels[i], i, pvowels + i, i, vowels + i);
        //pvowels + 1 and vowels + 1 are the same, this may confusing for the later but the name of the array itself is a constant pointer to the start of the array
    }

    // Print the values
    for (i = 0; i < 5; i++) 
    {
        printf("vowels[%d]: %c, *(pvowels + %d): %c, *(vowels + %d): %c\n", i, vowels[i], i, *(pvowels + i), i, *(vowels + i));
        //*(pvowels + i) can be used to call the ith term in an array
    }

    
    
    
    
    
    
    
    
    
    
    
    
    
    
}