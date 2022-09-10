import sys
import ecdsa
import base64

signature = sys.argv[1]
message = sys.argv[2]
pk_pem = '-----BEGIN PUBLIC KEY-----\nMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAE55/U4WPfQjltCrco5ndvJb6iZdkCvmM/\nAcIcn1i9j6EGN6Y5FLqo/TnNei5YoUxlxVgxBSF8aSS1tPJ/HRL18g==\n-----END PUBLIC KEY-----'
vk = ecdsa.VerifyingKey.from_pem(pk_pem)
result = False
try:
    result = vk.verify(base64.b64decode(signature), message.encode())
except:
    result = False
finally:
    print('Result', result)
