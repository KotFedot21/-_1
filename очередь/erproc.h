#ifndef ERPROC_H
#define ERPROC_H

#include <stdio.h>
#include "erproc.h"
#include <stdlib.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#include <string.h>

struct mymsgbuf {
        long mtype;
        char mtext[MAX_SEND_SIZE];
};


void send_message(int qid, struct mymsgbuf *qbuf, long type, char *text);
void read_message(int qid, struct mymsgbuf *qbuf, long type);
void remove_queue(int qid);
void change_queue_mode(int qid, char *mode);
void usage(void);

#endif 
