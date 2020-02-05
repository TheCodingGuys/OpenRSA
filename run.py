from lib.encryption import encryptAndWriteToFile, readFromFileAndDecrypt
from lib.commands import decrypt, encrypt, newusr, rmusr, _help, chkey
import os
import sys

encrypted_txt = 'msg/encrypted.txt'
decrypted_txt = 'msg/decrypted.txt'

priv_key = 'data/vsp_privkey.txt'
pub_key = 'data/vsp_pubkey.txt'

while True:
    cmd = input('>>> ').strip()

    if cmd == 'decrypt':
        decrypt()
    
    elif cmd == 'encrypt':
        encrypt()

    elif cmd == 'newusr':
        newusr()

    elif cmd == 'rmusr':
         rmusr()
        
    elif cmd == 'chkey':
        chkey()

    elif cmd == 'exit':
        sys.exit()
    
    elif cmd == 'help':
        _help()
    
    elif cmd != '':
        print('Command not found.')



