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
// ������� �� ��������� ���������� �����, �� ������� �� ������� ��� �������.
// ����� ���� �� ������ ������� (�� ���������) � ��������� ������.
// ����� �� ������� ������ �����������, ���� �����������, �� ��������� ����
// �� ��������� ����������� ������.
	for(step=1;step<=numOfStep;step++)
	{

		for (j=step-1;j<N-step+1;j++) // ���� ������.
		{
 array[step-1][j]=i++;
		}

		for (j=step;j<N-step+1;j++) // ���� ����
		{
 array[j][N-step]=i++;
		}

		for (j=N-step-1;j>=step-1;--j) // ���� �����, �����
		{
 array[N-step][j]=i++;
		}

		for (j=N-step-1;j>=step;j--) // ���� ����� �����
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
