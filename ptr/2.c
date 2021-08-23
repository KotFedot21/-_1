#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>



int main()
{

    char lspath[7]="/bin/ls";
    char pspath [7]="/bin/ps";
    int stat=0;
    pid_t pid1;

    pid1=fork();
    if(pid1==0)
    {
       int a=0;
       a=execl("/bin/ls","ls",NULL);
    }
    else
    {
        int b=0;
        b=execl("/bin/ps","ps", NULL);
    }
    return 0;

    wait(&stat);
}
