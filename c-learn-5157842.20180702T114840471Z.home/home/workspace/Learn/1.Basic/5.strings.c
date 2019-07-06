#include <stdio.h>
#include <string.h> //imports functions used on strings

int main()
{
    char string[] = "Hello World"; //Creates an array of characters, manifested as a string, array has a length of 11
    char * string2 = "Hello World"; //Creates an array with pointers instead
    printf("%s and %s\n", string, string2); //strings are printed with string formating 
    
    //String formatting//
    
    printf("%d\n", 1); // %d used as a place holder for where numbers will be placed
    printf("%s\n", "A"); // %s used as a place holder for where a character of string will be placed
    
    // \n is used to make program output on a newline
    
    //String formatting should be used with varaibles
    
    //Further Sting functions//
    
    printf("%lu\n", strlen(string)); //strlen fins how long a string is
    
    if (strncmp(string, string2, 11) == 0) { //strncmp compares 2 strings to see if they are the same, if they are it will return 0
    //a number can be supplied as the maximum comparison length 
        printf("same\n");
        
    char string3[16] = "Hello ";
    char string4[16] = "World";
    strncat(string3, string4, 16); //strncat takes arguments of starting string, adding string and maximum length to add; adds two strings together
    printf("%s",  string3);
    }
}