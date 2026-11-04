#include<stdio.h>
#include<stdlib.h>

// sudo bash build.sh
// echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

void vuln(){
    char buf[100];
    printf("buf addr: %p\n", buf);
    printf("input: ");
    gets(buf);
    printf("buf: %s\n", buf);
}

int main(){
    setregid(getegid(), getegid());
    vuln();
    puts("done");
    return 0;
}
