import hashlib
from colors import *
from pygments import console

def hash_encoder(hashtext):
    hashed = hashlib.md5(str(hashtext).encode())
    result = hashed.digest()
    print("\n  [ + ] hash → ", console.colorize("red", str(result)), "\n  [ + ] By default it is MD5")
hash_encoder(input("\n  Text: "))
