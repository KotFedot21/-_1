#include <unistd.h>
#include <stdio.h>

int main() {
    int fds[2] ;

    if (pipe(fds) == -1) {
        perror("pipe");
        return 1;
    }

    pid_t pid = fork();
    if (pid == -1) {
        perror("fork");
        return 1;
    }

    if (pid != 0) {
        if (dup2(fds[1], 1) == -1) {
            perror("dup2");
            return 1;
        }
        close(fds[0]);
        if (execlp("/bin/ls", "ls","-l", NULL) == -1) {
            perror("execlp");
            return 1;
        }
    } else {
        if (dup2(fds[0], 0) == -1) {
            perror("dup2");
            return 1;
        }
        close(fds[1]);
        if (execlp("/bin/grep", "grep", "-a", NULL) == -1) {
            perror("execlp");
            return 1;
        }
    }
}
