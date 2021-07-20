#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a = 0x00DDAABB;
    unsigned char c;
    c = (a& 0xFF);
    printf ( "First byte of a =%x\n",c);
    c = ((a>>8)& 0xFF);
    printf ( "Second byte of a =%x\n",c);
    c = ((a>>16)& 0xFF);
    printf ( "Third byte of a =%x\n",c);

    a = a & 0x00FFFFFF;
    printf("\nChanged number is %x\n ", a );

    return 0;
}
