from genqrcode import generate_qr_code
from aes import encrypt,decrypt
import base64
data=123
key = b'\xc2\xe2\xa8B\xf8#\x87\xe5\xe5\x9d\xee\xdc5\t\xf6\xe1/\x9af\x1c\xef\rP1\xce\xe1`\xa1\x89\x83C]'
iv = b'1234567891234567'
a= encrypt(str(data),key,iv)
print(a)