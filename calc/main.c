#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include "sum.h"
#include "div.h"
#include "mult.h"
#include "sub.h"
#include "get.h"
//#include <conio.h>



int main()
{
  setlocale(LC_ALL, "Rus");

  int selection;
  int a;
  int b;
  int s =0;
 // float z=0;


    while(selection!=5)
      {
          printf("\e[1;1H\e[2J") ;
          printf ("Что бы вы ходели сделать?\n 1. Cложить значения\n 2. Вычесть значения \n 3. Умножить значения\n 4. Поделить значения\n 5. Выход из программы");
          printf("\nВведите выбраный пункт:\n");
          scanf("%d",&selection);
                switch(selection)
                {
                    case 1:
                        get(&a, &b);
                        s=summ(&a, &b);
                        printf("%d+%d=%d\n",a,b,s);
                        getchar();
                        getchar();
                        break;
                    case 2:
                        get(&a, &b);
                        s= subtr(&a, &b);
                        printf("%d-%d=%d\n",a,b,s);
                        getchar();
                        getchar();
                        break;
                    case 3:
                        get(&a, &b);
                        s=mult(&a, &b);
                        printf("%d*%d=%d\n",a,b,s);
                        getchar();
                        getchar();
                        break;
                    case 4:
                        get(&a, &b);
                        s=divis(&a, &b);
                        printf("%d/%d=%d\n",a,b,s);
                        getchar();
                        getchar();
                        break;
                    case 5 :
                        selection=5;
                        exit;
                        break;

                    default:
                         printf( "Неправильный ввод.\n" );
                         selection=5;
                         break;



          }


      }

  return 0;
}
