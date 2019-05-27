#ifndef SCAFFOLD_H
#define SCAFFOLD_H

#ifdef __cplusplus
extern "C"
{
#endif
#define MAXBUF 256

int req(int sock, char *buf);
int ans(int sock, const char *buf);

#ifdef __cplusplus
} // extern "C"
#endif

#endif // !SCAFFOLD_H
