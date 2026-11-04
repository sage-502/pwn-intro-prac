#include <stdio.h>

// gcc -m32 -g -O0 -fno-pie -no-pie -mpreferred-stack-boundary=2 -fno-stack-protector -fno-omit-frame-pointer little.c -o little

int main() {
    int num = 0x41424344;
    char str[] = "ABCD";

    return 0;
}
