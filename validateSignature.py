import sys
import ecdsa
import base64

signature = sys.argv[1]
message = sys.argv[2]
pk_pem = open('./publicKey.pem').read()
vk = ecdsa.VerifyingKey.from_pem(pk_pem)
result = False
try:
    result = vk.verify(base64.b64decode(signature), message.encode())
except:
    result = False
finally:
    print('Result', result)
