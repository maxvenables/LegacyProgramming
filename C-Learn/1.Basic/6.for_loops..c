#include <stdio.h>
#include <string.h>

int main()
{
    for(int i = 0; i < 10; i++) //For loops run code multiple times until a condition is met. To make one we need 3 things:
    //Initialize the iterator variable using an initial value
    //Check if the iterator has reached its final value
    //Increases the iterator
    {
        printf("%d\n", i);
    }
    
    //We can also use for loops to generate arrays
    
    int numbers[10];
    for(int i = 0; i < 10; i++)
    {
        numbers[i] = i + 1;
    }
    
    //And we can print arrays with them too 
    
    for(int i = 0; i < 10; i++)
    {
        printf("%d\n", numbers[i]);
    }
}