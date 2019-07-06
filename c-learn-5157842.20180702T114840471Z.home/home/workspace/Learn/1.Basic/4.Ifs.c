#include <stdio.h>

int main()
{
    int age = 20;
    
    if (age > 50) //checks a condition
    {
        printf("You are old");
    }
    else if (age > 70) //checks another condition, if the "if" condition isnt met
    {
        printf("You are very old");
    }
    else //runs if no conditions are met
    {
        printf("You aren't old");
    }
}