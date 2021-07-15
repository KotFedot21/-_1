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
    // Заполнение массива
 for (i=0; i<SIZE; i++)  // цикл по строкам
    {
        for (j=0; j<SIZE; j++) // цикл по столбцам
        {
           u=u+1;         // увеличение параметра

           ARRAY[i][j]=u;
        }
    }
    // Вывод элементов массива
  for (i = 0; i<SIZE; i++)  // цикл по строкам
  {
    for (j = 0; j<SIZE; j++) // цикл по столбцам
    {
      printf("%d ", ARRAY[i][j]);
    }
    printf("\n"); // перевод на новую строку
  }
  getchar();
  return 0;
}

