#include <stdio.h>
#include <string.h>

typedef struct
{
    int x;
    int y;
}point;

void addonebyvalue(int x) //This function passes by value and does not work as intended as it does not change the actual value of the variable
{
    x++;
}

void addonebyreferance(int * x)//This function passes by reference using pointers, and thus it works as intended
{
    (*x)++; //Must be in brackets to work
}

void add(point * p) //If we want to alter multiple variables inside a struct we can just pass the struct instead of multiple pointers
{
    (*p).x++;
    (*p).y++;
    p->x++; //shortcut for above as it is so common
    p->y++;
}


int main()
{
    int n = 1;
    printf("n is equal to %d\n", n);
    addonebyvalue(n);
    printf("n is now still to %d\n", n);
    addonebyreferance(&n); //We must use & to signifie that its adress in memory is being passed
    printf("n is now equal to %d\n", n);
    
    point q;
    q.x = 0;
    q.y = 0;
    add(&q);
    printf("x is %d and y is %d", q.x, q.y);
    
}
