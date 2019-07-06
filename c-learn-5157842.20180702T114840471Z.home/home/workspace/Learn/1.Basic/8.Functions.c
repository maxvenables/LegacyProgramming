#include <stdio.h>
#include <string.h>

int function(int var); //Has to be created outside of main, can take an argument, should be created before filled with code
void function2(int var); //Function that returns nothing should be created with void

int main() 
{
    printf("%d\n", function(1));
    function2(1);
}

int function(int var) //Should be filled with code after main
{
    var += 1;
    return var;
}

void function2(int var)
{
    var += 2;
    printf("%d\n", var);
}