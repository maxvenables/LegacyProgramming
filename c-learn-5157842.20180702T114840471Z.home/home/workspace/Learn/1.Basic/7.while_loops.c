#include <stdio.h>
#include <string.h>

int main()
{
    //While loops iterate until a certain condition is met
    int i = 0;
    while (i < 10)
    {
        i++; //Variable must be iterated for the condition to be reached
    }
    
    printf("done\n");
    
    while (1) //Loops can be made to never finish if condition is never met, e.g. conditon is <> 0
    {
        printf("haha\n");
        i++;
        if (i > 20)
        {
            break; //break statements can be used to manually exit out of loop
        }
    }
    
    int j = 0;
    while (j < 10)
    {
        j++;
        if (j % 2 == 1) //Sets up condition, being if number is odd
        {
            continue; //Skips any code further down in the loop and starts a new iteration
        }
        printf("%d is  even\n", j);
    }
}