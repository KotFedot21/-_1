#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main()
{
    int SIZE = 3;
    int ARRAY[SIZE][SIZE];
    int i;
    int j;
    int u=0;
    // ���������� �������
 for (i=0; i<SIZE; i++)  // ���� �� �������
    {
        for (j=0; j<SIZE; j++) // ���� �� ��������
        {
           u=u+1;         // ���������� ���������

           ARRAY[i][j]=u;
        }
    }
    // ����� ��������� �������
  for (i = 0; i<SIZE; i++)  // ���� �� �������
  {
    for (j = 0; j<SIZE; j++) // ���� �� ��������
    {
      printf("%d ", ARRAY[i][j]);
    }
    printf("\n"); // ������� �� ����� ������
  }
  getchar();
  return 0;
}

