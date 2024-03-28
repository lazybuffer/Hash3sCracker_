#!/usr/bin/python3
#coding: utf-8

# # python_scripts
import hashlib
import sys
import os
from pygments import console

# manual text colored
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:

   type_hash = sys.argv[1]
   hash_a = sys.argv[2]

except:
   # # encoding part
   algorithms = hashlib.algorithms_guaranteed

   print(bcolors.BOLD+"""\n
   

   ███████╗███████╗███████╗███████╗███████╗███████╗███████╗███████╗███████╗███████╗
   ╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝

      """+bcolors.ENDC)

   print("   List OF Hash algorithmS: \n")
   for lst in algorithms:
      print(bcolors.OKGREEN+"    ",lst.lower()+bcolors.ENDC)
   # print(" ")

   print(bcolors.BOLD+"""
   ███████╗███████╗███████╗███████╗███████╗███████╗███████╗███████╗███████╗███████╗
   ╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝
   """+bcolors.ENDC)
   
   
   print(bcolors.FAIL+"""   
   """
   +
   str(os.system("cat banner/banner.txt"))
   +bcolors.BOLD+
   """  
      [ Hash3sCracker_ ]

   Author: Abhijit boro
   Instagram: https://www.instagram.com/_z3r0day_/
   Twitter: https://www.twitter.com/@0101Whoami
   
   """+bcolors.ENDC)


   print("  [ * ] USAGE: Just run python3 "+sys.argv[0]+" / To encode plain text and more..")
   print("  [ * ] USAGE: python3 "+sys.argv[0]+" [ hash_type ] which is do you wanna check [ your hash ] and hit enter \n")
   
   print("  [ # ] hashes.. (sha3_256, sha3_224, md5, shake_256, sha224, blake2s, blake2b) \n")
   print("  [ readme ] You must can use those are mention there \n")
   print("  [ 1 ] Do you want to encode plain text If Yes_! get space && hit Enter ")
   print("  [ 2 ] Do you want to encode Digest hashes..? type ( DIGESTHASH )")
   print("  [ 3 ] Do you want to identify hashes..? type ( IdentifyHASH )\n")
   print("  [ readme ] wordlist are major role in this software, without @ good wordlist and it is //shit// \n")

   print("  [ * ] Or if you wan2 cancel press ( CTL+C )\n")

   try:
      ask = input(bcolors.FAIL+"  Asking..? choose from readme"+bcolors.ENDC+"... ")
      if ask == " ":
         # your text to encode
         plain_text = input("\n  plain Text>_ ")

         # encode it to bytes using UTF-8 encoding
         text_to_encode = plain_text.encode()

         # hash with diff algorithms
         hashtype = input("\n  hash type>_ ")

         # md5 algorithm
         if hashtype == "md5":
            print(console.colorize("yellow","\n  [ + ] MD5: →"), console.colorize("red", hashlib.md5(text_to_encode).hexdigest()))
            sys.exit()

         # sha1 algorithm
         elif hashtype == "sha1":
            print(console.colorize("yellow","\n  [ + ] SHA1: →"), console.colorize("red", hashlib.sha1(text_to_encode).hexdigest()))
            sys.exit()

         # sha512 algorithm
         elif hashtype == "sha512":
            print(console.colorize("yellow","\n  [ + ] SHA512: →"), console.colorize("red", hashlib.sha512(text_to_encode).hexdigest()))
            sys.exit()

         # sha3_256 algorithm
         elif hashtype == "sha3_256":
            print(console.colorize("yellow","\n  [ + ] SHA3_256: →"), console.colorize("red", hashlib.sha3_256(text_to_encode).hexdigest()))
            sys.exit()

         # blake2s algorithm
         elif hashtype == "blake2s":
            print(console.colorize("yellow","\n  [ + ] BLAKE2S: →"), console.colorize("red", hashlib.blake2s(text_to_encode).hexdigest()))
            sys.exit()

         # blake2b algorithm
         elif hashtype == "blake2b":
            print(console.colorize("yellow","\n  [ + ] BLAKE2B: →"), console.colorize("red", hashlib.blake2b(text_to_encode).hexdigest()))
            sys.exit()

         # # shake_128 algorithm
         elif hashtype == "shake_128":
            print(console.colorize("yellow", "\n [ + ] SHAKE_128: →"), console.colorize("red", hashlib.shake_128(text_to_encode).hexdigest()))
            sys.exit()

         # sha3_224 algorithm
         elif hashtype == "sha3_224":
            print(console.colorize("yellow","\n  [ + ] SHA3_224: →"), console.colorize("red", hashlib.sha3_224(text_to_encode).hexdigest()))
            sys.exit()

         # SHA384 algorithm
         elif hashtype == "sha384":
            print(console.colorize("yellow","\n  [ + ] SHA384: →"), console.colorize("red", hashlib.sha384(text_to_encode).hexdigest()))
            sys.exit()

         # SHA3_384 algorithm
         elif hashtype == "sha3_384":
            print(console.colorize("yellow","\n  [ + ] SHA3_384: →"), console.colorize("red", hashlib.sha3_384(text_to_encode).hexdigest()))
            sys.exit()

         else:
            print(bcolors.FAIL+"\n  try @gain_! "+bcolors.ENDC)
            sys.exit()

      # for digest hashing...
      elif ask == "DIGESTHASH":
         import DigestHASHgenerator as advhash
         sys.exit()
      
      # for hash identifier
      elif ask == "IdentifyHASH":
         import hashidentifyer as identyhash
         sys.exit()

   except KeyboardInterrupt:
      #print(KeyboardInterrupt)
      print("\n\n " + bcolors.FAIL+" [ - ] Nothing choose from Above"+bcolors.ENDC)
      print("\n  Thanks for using "+ bcolors.FAIL+"HashesFinderDecoder_"+bcolors.ENDC, "\n")
      sys.exit()


# # decoding part
# READING MY WORDLIST TO FIND THE PASSWORD_!
wordlist = open('rockyou.txt', 'r').readlines()
for password in wordlist:
   password = password.strip()
   password = password.encode(encoding = 'UTF-8', errors = 'strict')
   
   try:      
      # MD5 ALGORITHM
      if type_hash == "md5":
         hash_b = hashlib.md5(password).hexdigest()
      
      # SHA1 ALGORITHM
      elif type_hash == "sha1":
         hash_b = hashlib.sha1(password).hexdigest()
      
      # SHA512 ALGORITHM
      elif type_hash == "sha512":
         hash_b = hashlib.sha512(password).hexdigest()
      
      # SHA384 ALGORITHM
      elif type_hash == "sha384":
         hash_b = hashlib.sha384(password).hexdigest()
      
      # SHA3_256 ALGORITHM
      elif type_hash == "sha3_256":
         hash_b = hashlib.sha3_256(password).hexdigest()
      
      # BLAKE2S ALGORITHM
      elif type_hash == "blake2s":
         hash_b = hashlib.blake2s(password).hexdigest()
      
      # BLAKE2B ALGORITHM
      elif type_hash == "blake2b":
         hash_b = hashlib.blake2b(password).hexdigest()
      
      # BLAKE2S ALGORITHM
      elif type_hash == "sha3_224":
         hash_b = hashlib.sha3_224(password).hexdigest()

      # SHA3_384 ALGORITHM
      elif type_hash == "sha3_384":
         hash_b = hashlib.sha3_384(password).hexdigest()
      
      # SHA256 ALGORITHM
      elif type_hash == "sha256":
         hash_b = hashlib.sha256(password).hexdigest()

   except Exception as e:
      print("\n " + bcolors.FAIL+" [ - ] Nothing choose from Above"+bcolors.ENDC)
      print("\n  [ + ] Thanks for using "+ bcolors.FAIL+"HashesFinderDecoder_"+bcolors.ENDC+"\n")
      sys.exit()
   
   try:
      # RESULT POINT
      if hash_a == hash_b:
         print("""
  [ + ] ############################################
  [ + ] ############################################
  [ + ] ############################################
  [ + ] #########""", bcolors.ENDC+ console.colorize("yellow", "key found"), "[ ", password," ]", """#########
  [ + ] ############################################
  [ + ] ############################################
  [ + ] ############################################
        """)
         sys.exit()
      else:
         print("  [ - ] not found_? : ", password)
   except KeyboardInterrupt:
      print(KeyboardInterrupt)
      print("\n  [ + ] Thanks for using "+ bcolors.FAIL+"HashesFinderDecoder_"+bcolors.ENDC+"\n")
      sys.exit()
      
