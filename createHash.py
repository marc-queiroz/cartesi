# Reference: https://solidity-by-example.org/signature/

from eth_abi.packed import encode_packed
from Crypto.Hash import keccak

k = keccak.new(digest_bits=256)
k.update(encode_packed(['address','uint','string','uint'],['0x14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C', 123, 'coffee and donuts', 1]))
print('HASHED MESSAGE: ', k.hexdigest())
