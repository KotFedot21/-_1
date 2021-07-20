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
    // Çàïîëíåíèå ìàññèâà
 for (i=0; i<SIZE; i++) // öèêë ïî ñòðîêàì
    {
        for (j=0; j<SIZE; j++) // öèêë ïî ñòîëáöàì
        {
 u=u+1; // óâåëè÷åíèå ïàðàìåòðà

 ARRAY[i][j]=u;
        }
    }
    // Âûâîä ýëåìåíòîâ ìàññèâà
  for (i = 0; i<SIZE; i++) // öèêë ïî ñòðîêàì
  {
    for (j = 0; j<SIZE; j++) // öèêë ïî ñòîëáöàì
    {
      printf("%d ", ARRAY[i][j]);
    }
    printf("\n"); // ïåðåâîä íà íîâóþ ñòðîêó
  }
  getchar();
  return 0;
}
