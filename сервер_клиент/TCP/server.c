#include <sys/types.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include "erproc.h"
#define PORT     34543
#define MAXLINE 1024

int main ()
{
	int server = Socket (AF_INET,SOCK_STREAM,0);
	struct sockaddr_in adr={0};//ipV4
	adr.sin_family=AF_INET;
	adr.sin_port=htons(PORT);
	Bind (server,(struct sockaddr*) &adr, sizeof adr);
	Listen(server,5);
    socklen_t adrlen = sizeof adr;
	int fd=Accept(server , (struct sockaddr *) &adr, &adrlen);
	ssize_t nread;
	char buf[MAXLINE];
	nread=read(fd, buf, MAXLINE;
	if (nread ==-1){
		perror("read failed");
		exit (EXIT_FAILURE);
	}
	if (nread==0){
		printf("END of  FILE\n");
	}
	write(STDOUT_FILENO, buf, nread );
	
	write(fd, buf, nread);

	sleep(1);
	close(fd);

	close(server);
	return 0;
}
