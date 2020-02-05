from .encryption import encryptAndWriteToFile, readFromFileAndDecrypt
from .files import mkfile
from .keys import makeKeyFiles
from shutil import rmtree
import os


def encrypt():
    """Encrypts a file to a specified user."""

    user = input('Encrypt message to user: ').strip()

    if os.path.exists(f'./users/{user}/') or user == 'me':
        # if the user is yourself
        if user == 'me':
            # check if file is empty
            if os.stat('./me/encrypted.txt').st_size == 0:
                print('./me/encrypted.txt is empty. Nothing to encrypt.')
                return
            
            # writes encrypted message to file
            with open('./me/encrypted.txt') as f:
                encryptAndWriteToFile('./me/encrypted.txt', './me/keys/me_pubkey.txt', f.read())
                return

        elif user != 'me':
            # if the file is empty just lets the user know
            if os.stat(f'./users/{user}/encrypted.txt').st_size == 0:
                print(f'./users/{user}/encrypted.txt is empty. Nothing to encrypt.')
                return

            with open(f'./users/{user}/encrypted.txt') as f:
                try:
                    encryptAndWriteToFile(f'./users/{user}/encrypted.txt',  f'./users/{user}/pubkey.txt', f.read())
                except Exception:
                    print(f'Public key is not set! Goto \'./users/{user}/pubkey.txt\' to write the key.')

            # lets the user know that the file was encrypted successfully
            print('Successfully wrote encrypted message to \'./me/encrypted.txt\'.')
            return
    
    print('User not found.')


def decrypt():
    """Decrypts a file from a specified user."""

    user = input('Decrypt message from user: ').strip()

    if os.path.exists(f'./users/{user}/') or user == 'me':
        # if the user is yourself
        if user == 'me':
            encrypted_file = f'./me/encrypted.txt'
            
            # decrypts message and writes it to ./me/decrypted.txt
            with open(f'./me/decrypted.txt', 'w') as f:
                f.write(readFromFileAndDecrypt(encrypted_file, './me/keys/me_privkey.txt'))

            # if succeeded then print it was a success
            print(f'Successfully decrypted message at /me/decrypted.txt')
            return
            
        elif os.path.exists(f'./users/{user}'):
            encrypted_file = f'./users/{user}/encrypted.txt'
            
            # decrypts message and writes it to ./users/(user)/decrypted.txt
            with open(f'./users/{user}/decrypted.txt', 'w') as f:
                f.write(readFromFileAndDecrypt(encrypted_file, './me/keys/me_privkey.txt'))

            # if succeeded then print it was a success
            print(f'Successfully decrypted message at /users/{user}/decrypted.txt')
            return

    print('User not found.')


def newusr():
    """Adds a new user to directory 'users'."""

    username = input('New user: ').strip()

    # the path where the directory is going to be
    path = f'./users/{username}/'

    os.mkdir(path)

    # this is will create three files: their public key and their encrypted message and the decrypted message
    mkfile(path + 'pubkey.txt'), mkfile(path + 'encrypted.txt'), mkfile(path + 'decrypted.txt')

    print(f'Make sure to write the public key to \'./users/{username}/pubkey.txt\'')


def rmusr():
    """Removes a user by name."""

    username = input('Remove user: ')
    
    if os.path.exists(f'./users/{username}'):
        sure = input(f'Are you sure you want to remove user {username}? [y/n] ').strip().lower()

        if sure == 'y':
            rmtree(f'./users/{username}')
        
            print(f'Successfully removed user {username}.')
    
    else:
        print('User not found')


def chkey():
    """Changes current encryption and decryption key."""

    print('WARNING: THIS WILL CHANGE THE CURRENT ENCRYPTION AND DECRYPTION KEY')
    print('WARNING: THIS ACTION CAN NOT BE UNDONE')

    # prompts the user for key size
    key_size = input('Key size (default is 1024): ')
    sure = input('Are you sure you want to change the current key? [y/n] ').strip().lower()

    if sure == 'y':
        # if the user didn't specify a key size just use the default
        if not key_size:
            key_size = 1024

        makeKeyFiles('./me/keys/me', int(key_size))

        print('Successfully changed key.')


def _help():
    """Displays this message."""

    print(f"""encrypt - {encrypt.__doc__}
decrypt - {decrypt.__doc__}
newusr - {newusr.__doc__}
rmusr - {rmusr.__doc__}
help - {_help.__doc__}

-- ADVANCED --
chkey - {chkey.__doc__}
""")
