#include <stdio.h>
#include <string.h>
#include <stdlib.h> //needed for "molloc" and "free"

typedef struct
{
    char * name;
    int age;
}
person;

int main()
{
    person * myperson = malloc(sizeof(person)); //Dynamically allocates as much memory as "myperson" needs
    //"sizeof(person)" tells "malloc" exactly how much memory is needed for person
    
    myperson->name = "Jeff"; //Can use -> shortcut
    myperson->age = 48;
    
    printf("My name %s, age: %d", myperson->name, myperson->age);
    
    free(myperson); //after we are done using "myperson" we free the pointer of pointing to the memory, this means the data of myperson still exists but it cannot be accsessed by "myperson"
    
}