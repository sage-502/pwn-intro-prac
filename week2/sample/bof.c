#include <stdio.h>

// gcc -m32 -O0 -fno-pie -no-pie -mpreferred-stack-boundary=2 -fno-stack-protector -fno-omit-frame-pointer bof.c -o bof

void vuln(){
	char buf[12];
	printf("input: ");
	gets(buf);
}

int main(){
	vuln();
	puts("done");
	return 0;
}
