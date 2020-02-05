from .encryption import encryptAndWriteToFile, readFromFileAndDecrypt
from .files import mkfile
from .keys import makeKeyFiles
from shutil import rmtree
import os
import sys


def encrypt():
    """Encrypts a file to a specified user."""

    user = input('Encrypt message to user: ').strip()

    if os.path.exists(f'./users/{user}/') or user == 'me':
        # if the user is yourself
        if user == 'me':
            # check if file is empty
            if os.stat('./me/encrypted.txt').st_size == 0:
                return './me/encrypted.txt is empty. Nothing to encrypt.'
            
            # writes encrypted message to file
            with open('./me/encrypted.txt') as f:
                encryptAndWriteToFile('./me/encrypted.txt', './me/keys/me_pubkey.txt', f.read())

        elif user != 'me':
            # if the file is empty just lets the user know
            if os.stat(f'./users/{user}/encrypted.txt').st_size == 0:
                return f'./users/{user}/encrypted.txt is empty. Nothing to encrypt.'

            with open(f'./users/{user}/encrypted.txt') as f:
                try:
                    encryptAndWriteToFile(f'./users/{user}/encrypted.txt',  f'./users/{user}/pubkey.txt', f.read())
                except Exception:
                    return f'Public key is not set! Goto \'./users/{user}/pubkey.txt\' to write the key.'

            # lets the user know that the file was encrypted successfully
            return 'Successfully wrote encrypted message to \'./me/encrypted.txt\'.'
    
    return 'User not found.'


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
            return f'Successfully decrypted message at /me/decrypted.txt'
            
        encrypted_file = f'./users/{user}/encrypted.txt'
            
        # decrypts message and writes it to ./users/(user)/decrypted.txt
        with open(f'./users/{user}/decrypted.txt', 'w') as f:
            f.write(readFromFileAndDecrypt(encrypted_file, './me/keys/me_privkey.txt'))

        # if succeeded then return it was a success
        return f'Successfully decrypted message at /users/{user}/decrypted.txt'

    return 'User not found.'


def newusr():
    """Adds a new user to directory 'users'."""

    username = input('New user: ').strip()

    # the path where the directory is going to be
    path = f'./users/{username}/'

    os.mkdir(path)

    # this is will create three files: their public key and their encrypted message and the decrypted message
    mkfile(path + 'pubkey.txt'), mkfile(path + 'encrypted.txt'), mkfile(path + 'decrypted.txt')

    return f'Make sure to write the public key to \'./users/{username}/pubkey.txt\''


def rmusr():
    """Removes a user by name."""

    username = input('Remove user: ')
    
    if os.path.exists(f'./users/{username}'):
        sure = input(f'Are you sure you want to remove user {username}? [y/n] ').strip().lower()

        if sure == 'y':
            rmtree(f'./users/{username}')
        
            return f'Successfully removed user {username}.'
    
    else:
        return 'User not found'


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

        return 'Successfully changed key.'


def _exit():
    """Terminates."""

    sys.exit()


def _help():
    """Displays this message."""

    return f"""encrypt - {encrypt.__doc__}
decrypt - {decrypt.__doc__}
newusr - {newusr.__doc__}
rmusr - {rmusr.__doc__}
help - {_help.__doc__}
exit - {_exit.__doc__}

-- ADVANCED --
chkey - {chkey.__doc__}
"""


############################## code below is not considered commands ##############################

# all valid commands 
valid_commands = {
    'decrypt': decrypt,
    'encrypt': encrypt,
    'newusr': newusr,
    'rmusr': rmusr,
    'help': _help,
    'chkey': chkey,
    'exit': _exit,
}


def call_command(command):
    """Checks if the parameter 'command' is a valid command."""

    if command:
        # loops over all valid commands
        for cmd in valid_commands.keys():
            # if the command is valid
            if cmd == command:
                return valid_commands[cmd]

        return f'\'{command}\' command not found'


