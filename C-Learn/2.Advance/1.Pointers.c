#include <stdio.h>
#include <string.h>

int main()
{
    int a = 10; //normal variable
    int * pointer_to_a = &a; //Pointer is dereferenced (shows where the pointer points to) with *. Value pointed to is done with &
    printf("a is equal to %d\n", a);
    printf("a is also equal to %d\n", *pointer_to_a); //* must be placed before pointer to indicate we want the value, not the position
    
    //We can also change the value of a with the pointer
    
    a += 10; //Normal way
    *pointer_to_a += 10; //Pointer way
    
    printf("%d\n", *pointer_to_a); //should be 30
}