#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include "scaffold.h"

int req(int sock, char *buf)
{
    int n;

    if (write(sock, buf, strlen(buf)) < 0)
        return -1;
    
    bzero(buf, MAXBUF);
    if ((n = read(sock, buf, MAXBUF)) < 0)
        return -2;

    buf[MAXBUF-1]='\0';
    return n;
}

int ans(int sock, const char *buf)
{
    return write(sock, buf, strlen(buf));
}
