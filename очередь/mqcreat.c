#include <stdio.h>
#include "erproc.h"
#include <stdlib.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#define MAX_SEND_SIZE 80
#include <string.h>

struct mymsgbuf {
	long mtype;
	char mtext[MAX_SEND_SIZE];
};
int main(int argc, char *argv[])
{
	key_t key;
	int msgqueue_id;
	struct mymsgbuf qbuf;

	if(argc == 1)
		usage();

	/* Создаем уникальный ключ через вызов ftok() */
	key = ftok(".",'m');

	/* Открываем очередь - при необходимости создаем */
	if((msgqueue_id = msgget(key, IPC_CREAT|0660)) == -1) {
		perror("msgget");
		exit(1);
	}

	switch(tolower(argv[1][0]))
	{
		case 's': send_message(msgqueue_id, (struct mymsgbuf *)&qbuf,
					  atol(argv[2]), argv[3]);
			  break;
		case 'r': read_message(msgqueue_id, &qbuf, atol(argv[2]));
			  break;
		case 'd': remove_queue(msgqueue_id);
			  break;
		case 'm': change_queue_mode(msgqueue_id, argv[2]);
			  break;
		default:  usage();
	}   return(0);
}



