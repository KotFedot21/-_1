#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#include "erproc.h"

#define PORT     34543
#define MAXLINE 1024


int main ()
{
	int fd = Socket (AF_INET, SOCK_STREAM, 0);
	struct sockaddr_in adr ={0};
	adr.sin_family=AF_INET;// IPV4
	adr.sin_port=htons(PORT);
	Inet_pton(AF_INET,"127.0.0.1",&adr.sin_addr);
        Connect(fd, (struct sockaddr *)&adr, sizeof adr);	
	write (fd, "Hello\n",6);
	char buf[MAXLINE];
	ssize_t nread;
	nread=read(fd, buf,MAXLINE);
	if (nread ==-1){
		perror("read failed");
		exit(EXIT_FAILURE);
	}
	if(nread ==0){
		printf("EOF occured\n");
	}
	write(STDOUT_FILENO,buf, nread);
	close(fd);
	return 0;

}
