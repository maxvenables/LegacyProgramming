#include <stdio.h>
#include <string.h>

struct point //A simple structure that only holds an x and y value, very commonly used
{
    int x;
    int y;
};

typedef struct //typedef keyword allows us to define types with different names
{
    int x;
    int y;
}point1; //name is defined after curly braces

typedef struct
{
    char * name; //Structs can also hold pointers, which can be to strings, or most importantly other structs
    int age;
}person;

int main()
{
    struct point p; // Creates a new object of point inside the main
    p.x = 10; //We can change the value of an objects variables
    p.y = 10; //We access the objects variables with the . operator
    
    point1 p1; // Typedef This allows us to shortern the definition of a structure
    p1.x = 10;
    p1.y = 10;
    
    person man;
    man.name = "jeff";
    man.age = 22;
}