#include <stdio.h>
#include <stdlib.h>

int main()
{
    int SIZE = 5;
    int ARRAY[SIZE][SIZE];
    int i, j;

    for ( i=0; i<SIZE; i++)  // ������� ������� �������
    {
        for ( j=0; j<SIZE; j++)
        {
            ARRAY[i][j]=0;

            printf("%d ", ARRAY[i][j]);
        }

        printf("\n");

    }

    printf("\n"); // �������� �� 2-�� �������
    printf("\n");

    for ( i=0; i<SIZE; i++) // ����������� �������
    {
        for ( j=0; j<=i; j++)

        {
            ARRAY[i][j]=1;

        }

     }

        for ( i=0; i<SIZE; i++) // ����� �������
    {
        for ( j=0; j<SIZE; j++)

        {
            printf("%d ", ARRAY[i][j]);
        }

        printf("\n");
     }


    return 0;
}
