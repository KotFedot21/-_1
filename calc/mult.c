#include <stdio.h>
#include <stdlib.h>

int mult (int *a, int *b)
{
    int s=0;


    s=(*a)*(*b);
    //printf("%d*%d=%d\n",*a,*b,s);
    return s;
}


