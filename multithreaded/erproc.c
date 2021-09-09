#include "erproc.h"
#include <sys/types.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>

int Socket (int domain, int type, int protocol)
{
	int result=socket (domain, type, protocol);
	if (result== -1)
	{
		perror("socket faild");
		exit (EXIT_FAILURE);
	}
	return result ;
}


void Bind (int sockfd, const struct sockaddr *addr, socklen_t addrelen)
{
	int result =bind(sockfd, addr, addrelen);
	if (result ==-1)
	{
		perror("bind failed");
		exit (EXIT_FAILURE);
	}
}
void Listen(int sockfd, int baklog)
{
	int result=listen(sockfd, baklog);
	if (result==-1){
		perror("listen failed");
	}
}

int Accept (int sockfd, struct sockaddr *addr, socklen_t *addrlen)
{
	int result= accept (sockfd, addr, addrlen);
	if(result==-1){
		perror("accept failed");
			exit(EXIT_FAILURE);
	}
	return result;
}

void Connect (int sockfd, const struct sockaddr *addr, socklen_t addrlen)
{
	int res =connect(sockfd, addr, addrlen);
	if (res==-1){
		perror("connect filed");
		exit(EXIT_FAILURE);
	}
}
void Inet_pton (int af, const char *src, void *dst)
{
	int res = inet_pton(af,src, dst);
       if (res==0){
	       printf("inet_pton faild 1");
	       exit(EXIT_FAILURE);

       }
	if (res==-1){
		perror ("inet_pton faild");
		exit(EXIT_FAILURE);
}
}
