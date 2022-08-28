import re

from colors import *

HASH_TYPE_REGEX = {
    re.compile(r"^[a-fA-F\d]{32}(:.+)?$", re.IGNORECASE): ["MD4", "MD2", "Double MD5", "MD5"],
    re.compile(r"^[a-f0-9]{64}(:.+)?$", re.IGNORECASE): ["RIPEMD-256", "SHA3-256", "Haval-256","SHA-256"],
    re.compile(r"^[a-f0-9]{40}(:.+)?$", re.IGNORECASE): ["SHA1", "MySQL4.1/MySQL5", "SHA1(UTF16-LE($plaintext))"],
    re.compile(r"^[a-f0-9]{96}(:.+)?$", re.IGNORECASE): ["SHA3_384", "SHA384"],
    re.compile(r"^[a-f0-9]{128}(:.+)?$", re.IGNORECASE): ["SHA-512", "Whirlpool", "Salsa10","Salsa20", "SHA3-512", "Skein-512","Skein-1024(512)"],
}

# Function
def custom_hash_identifier(hashed_text):
     result = [ HASH_TYPE_REGEX[algo] for algo in HASH_TYPE_REGEX if algo.match(hashed_text)]
     print("\n  [ + ] Possible hash type", bcolors.FAIL+str(result)+bcolors.ENDC)

hashtxt = input("\n  Your Hash: ")

# ex1 = '67881381dbc68d4761230131ae0008f7'
# ex1 = 'f396c5df2b7c3db9a2b8cc44f2736be8bd113cdb5ab9e99c5cd8eb2d3fb9bbb0'

custom_hash_identifier(hashtxt)

print("\n  [ + ] ", len(hashtxt) * int(4), bcolors.FAIL+"bit hash"+bcolors.ENDC)
