#include<stdio.h>
#include<unistd.h>

int main(){
    pid_t fpid;
    int count = 0;
    while(fpid = fork());
    printf("fpid: %d \t pid: %d \n", fpid, getpid());
    count++;
    printf("count:%d\n",count);
    return 0;
}