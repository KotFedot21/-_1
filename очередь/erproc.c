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


void send_message(int qid, struct mymsgbuf *qbuf, long type, char *text)
{
	/* Посылаем сообщение в очередь */
	printf("Sending a message ...\n");
	qbuf->mtype = type;
	strcpy(qbuf->mtext, text);

	if((msgsnd(qid, (struct msgbuf *)qbuf,
					strlen(qbuf->mtext)+1, 0)) == -1)
	{
		perror("msgsnd");
		exit(1);
	}
}

void read_message(int qid, struct mymsgbuf *qbuf, long type)
{
	/* Вычитываем сообщение из очереди */
	printf("Reading a message ...\n");
	qbuf->mtype = type;
	msgrcv(qid, (struct msgbuf *)qbuf, MAX_SEND_SIZE, type, 0);

	printf("Type: %ld Text: %s\n", qbuf->mtype, qbuf->mtext);
}

void remove_queue(int qid)
{
	/* Удаляем очередь */
	msgctl(qid, IPC_RMID, 0);
}

void change_queue_mode(int qid, char *mode)
{
	struct msqid_ds myqueue_ds;

	/* Получаем текущее состояние */
	msgctl(qid, IPC_STAT, &myqueue_ds);

		/* Меняем состояние в копии внутренней структуры данных */
		sscanf(mode, "%o", &myqueue_ds.msg_perm.mode);

		/* Обновляем состояние в самой внутренней структуре данных */
		msgctl(qid, IPC_SET, &myqueue_ds);
}

void usage(void)
{
	fprintf(stderr, "msgtool - A utility for tinkering with msg queues\n");
	fprintf(stderr, "\nUSAGE: msgtool (s)end  \n");
	fprintf(stderr, "                 (r)ecv \n");
	fprintf(stderr, "                 (d)elete\n");
	fprintf(stderr, "                 (m)ode \n");
	exit(1);
}

