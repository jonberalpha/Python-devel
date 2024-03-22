Requirements:
  pycryptodome

First do encryption of the file "message.png" with
  python secure_session.py
  
  -> creates file "encrypted.bin" in same directory

Afterwards execute attack with
  python attack.py

Description:
  Attack-Script reads the creation data of the encrypted.bin
  and a base string is built from it but without using seconds and microseconds
  Than it brute forces (loops through) the seconds and microseconds to find 
  the correct unique seed. Moreover a sec_offset variable can be set in the code
  just to speed things up
