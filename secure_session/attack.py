from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from os import path
from datetime import datetime, timedelta
import time

# read encrypted.bin
with open("encrypted.bin", "rb") as f:
    ciphertext = f.read()

# get creation time/date details of encrypted.bin
creation_time = datetime.fromtimestamp(path.getmtime("encrypted.bin"))

# initialize number of tries, offset seconds and start time
num_tries = 0
sec_offset = 0
start_time = time.time()

# iterate over all possible seconds and microseconds
for sec in range(sec_offset, 60):
    for microsec in range(1000000):
        num_tries += 1
        unique_seed = creation_time.strftime("%Y-%m-%d_%H:%M:") + "{:02d}.{:06d}".format(sec, microsec)
        hash_object = SHA256.new(data=unique_seed.encode())
        session_key = hash_object.digest()
        cipher = AES.new(session_key, AES.MODE_CBC, IV=bytes(16))
        decrypted_data = cipher.decrypt(ciphertext)

        # check if decrypted data starts with "SESSION_OPEN:"
        if decrypted_data.startswith(b'SESSION_OPEN:'):
            # write decrypted data to a file without "SESSION_OPEN:"-prefix
            with open("decrypted.png", "wb") as f:
                f.write(decrypted_data[len(b'SESSION_OPEN:'):])
            # finally print results
            print("Decryption successful for seed:", unique_seed, end=', ')
            print("Time elapsed:", timedelta(seconds=time.time() - start_time), end=', ')
            print("Number of tries:", num_tries)
            break
        else:
            # calculate time elapsed each iteration
            elapsed_time_t = time.time() - start_time
            hours, remainder = divmod(elapsed_time_t, 3600)
            minutes, seconds = divmod(remainder, 60)
            elapsed_time = "{}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
            # print decryption progress
            print(f"Elapsed time: {elapsed_time}, Iteration: {num_tries}, Unique seed: {unique_seed}", end='\r')
    else:
        continue
    break

