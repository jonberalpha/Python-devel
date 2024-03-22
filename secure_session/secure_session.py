from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import datetime

# https://www.pycryptodome.org/src/cipher/cipher

# The first few bytes are constant so that it
# can be checked if brute force decryption worked
data = b'SESSION_OPEN:'

with open("message.png", "rb") as f:
    while True:
        chunk = f.read(1024)
        if len(chunk) <= 0:
            break
        data += chunk

data += bytes(16 - (len(data) % 16))

# Derive unique 256-bit session key
d = datetime.datetime.now()

# This is easier to brute-force, as we are only using seconds
#unique_seed = d.strftime("%Y-%m-%d_%H:%M:%S")

# This is by a factor of 1 mio tougher/slower, since we include microseconds
unique_seed = d.strftime("%Y-%m-%d_%H:%M:%S.%f")

print("Unique seed: " + unique_seed)
hash_object = SHA256.new(data=unique_seed.encode())
session_key = hash_object.digest()
cipher = AES.new(session_key, AES.MODE_CBC, IV=bytes(16))
ciphertext = cipher.encrypt(data)

with open("encrypted.bin", "wb") as fenc:
  fenc.write(ciphertext)
