#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int get(int *a, int*b)
{
  printf("введите значение а\n");
  scanf("%d",a);
  printf("введите значение b\n");
  scanf("%d",b);
  return 0;
}
