import sys
import ecdsa
import base64
message = sys.argv[1]
sk_pem = open('./privateKey.pem').read()
sk = ecdsa.SigningKey.from_pem(sk_pem)
signature = sk.sign(message.encode())
print("Signed Message:", base64.b64encode(signature).decode())
