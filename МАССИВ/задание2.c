#include <stdio.h>
#include <stdlib.h>

int main()
{
    int SIZE = 6;
    int ARRAY[SIZE];
    int i, j, tmp;
    int u=0;

    for (i=0; i<SIZE; i++ )
    {
        u=u+1;
        ARRAY[i]=u;
        printf("%d", ARRAY[i]);
    }

    printf("\n");

     for (i = 0, j = SIZE - 1; i < SIZE/2; i++, j--)
    {
        tmp = ARRAY[i];
        ARRAY[i] = ARRAY[j];
        ARRAY[j] = tmp;
    }

    for (i=0; i<SIZE; i++)
    {
        printf("%d", ARRAY[i]);
    }


    return 0;
}
