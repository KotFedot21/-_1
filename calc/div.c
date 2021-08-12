#include <stdio.h>
#include <stdlib.h>

struct function_name
{
    char *name[20];
}



int divis (int *a, int *b)
{
    int s=0;


    s=(*a)/(*b);//приведение к другому типу
    //printf("%d/%d=%f\n",*a,*b,s);
    return s;
}
