#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int main()
{
    int stat=0;
    pid_t pid1;
    pid1=fork();



    if (pid1==0)
    {
        pid_t pid2;
        printf("i am child 2 , my pid%d PPID%d\n", getpid(), getppid());
        pid2=fork();
        if(pid2==0)
        {
            printf("i am child 4, my pid%d PPID%d\n", getpid(), getppid());
            wait(&stat);
        }

    }else
    {
        pid_t pid3;
        printf("a parent 1, my pid=%d PPID=%d\n", getpid(), getppid());
        pid3=fork();

        if (pid3==0)
        {
            pid_t pid4;
            printf("i am child 3, my pid%d PPID%d\n", getpid(), getppid());
            pid4=fork();

            if(pid4==0)
            {
             printf("i am child 5, my pid%d PPID%d\n", getpid(), getppid());
            }
            else
                {
                 pid_t pid5;
                 pid5=fork();
                if(pid5==0)
            {
             printf("i am child 6, my pid%d PPID%d\n", getpid(), getppid());
            }
            else
                {

            wait(&stat);
               }
               }

    }
    }

    wait(&stat);
    //printf("Hello world!\n");
    return 0;

}
