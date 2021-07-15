#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N=8;
    int array[N][N];
	int i=1;
	int j;
	int step;
	int numOfStep=N/2;
// Сначала мы вычисляем количество шагов, за которые мы обойдем всю матрицу.
// Потом идем до границ матрицы (по периметру) и заполняем ячейки.
// Когда мы пройдем четыре направления, цикл повторяется, на последнем шаге
// мы заполняем центральную ячейку.
	for(step=1;step<=numOfStep;step++)
	{

		for (j=step-1;j<N-step+1;j++) // Идем вправо.
		{
 array[step-1][j]=i++;
		}

		for (j=step;j<N-step+1;j++) // Идем вниз
		{
 array[j][N-step]=i++;
		}

		for (j=N-step-1;j>=step-1;--j) // Идем влево, снизу
		{
 array[N-step][j]=i++;
		}

		for (j=N-step-1;j>=step;j--) // Идем вверх слева
		{
 array[j][step-1]=i++;
		}
	}

	if (N%2!=0)
	{
 array[N/2][N/2] = N*N;
	}

	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			printf("\t%d\t ",array[i][j]);
		}
		printf("\n");
	}

return 0;

}
