#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main()
{
    unsigned int multiply(unsigned int x, unsigned int y)
    {
        if (x == 1) //Creates exit clause
        {
            return y;
        }
        else if (x > 1)
        {
            return y + multiply(x-1, y);//Calls function inside itself
        }
        return y;
    }
    
    
    printf("3 * 5 = %u", multiply(3, 5));
    
}