//Задание: создать 2 процесса и передать между ними сообщение через канал 

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
     int fd[2], nbytes;
     pipe(fd);
     char string[] ="Hello papa!\n";
     char buf[80];

    pid_t child_pid=fork();
    if(child_pid<0){
        perror("fork() faild");
        exit (EXIT_FAILURE);
    }
    else if (child_pid==0){//потомок
        close(fd[0]);
        write(fd[1],string, strlen(string));
        exit(0);
        }
    else if (child_pid>0){//родитель
        close(fd[1]);
        nbytes = read(fd[0],buf,sizeof(buf));
        printf("the descendant said: %s",buf);
    }
  
    return 0;
}
