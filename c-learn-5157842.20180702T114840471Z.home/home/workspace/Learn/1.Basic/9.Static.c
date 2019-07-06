#include <stdio.h>
#include <string.h>

//The static keyword increases the scope of a variable up to the file they are contained in , meaning the variable can be accsessed anywher in the file

int iterate();
static void func();

int main()
{
    printf("%d\n", iterate());
    printf("%d\n", iterate());
}

int iterate()
{
    static int i = 0;//Static prevents counter reseting every time function is called
    i ++;
    return i;
}

static void func()//Making a function static means a function can only be accsessed inside a file, unlike global functions
{
    printf("I'm a static function");
}