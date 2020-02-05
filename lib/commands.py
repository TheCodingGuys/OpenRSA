from .encryption import encryptAndWriteToFile, readFromFileAndDecrypt
from .files import mkfile
from shutil import rmtree
import os


def encrypt():
    """Encrypts a file to a specified user."""

    user = input('Encrypt message to user: ').strip()

    # if the user is yourself
    if user == 'me':
        # check if file is empty
        if os.stat('./me/encrypted.txt').st_size == 0:
            print('./me/encrypted.txt is empty. Nothing to encrypt.')
            return
        
        # writes encrypted message to file
        with open('./me/encrypted.txt') as f:
            encryptAndWriteToFile('./me/encrypted.txt', './me/keys/vsp_pubkey.txt', f.read())

    elif user != 'me':
        # if the file is empty just lets the user know
        if os.stat(f'./users/{user}/encrypted.txt').st_size == 0:
            print(f'./users/{user}/encrypted.txt is empty. Nothing to encrypt.')
            return

        with open('./me/encrypted.txt') as f:
            encryptAndWriteToFile('./me/encrypted.txt', './me/keys/vsp_pubkey.txt', f.read())

        # lets the user know that the file was encrypted successfully
        print('Successfully wrote encrypted message to \'./me/encrypted.txt\'.')


def decrypt():
    """Decrypts a file from a specified user."""

    user = input('Decrypt message from user: ').strip()

    # if the user is yourself
    if user == 'me':
        encrypted_file = f'./me/encrypted.txt'
        
        # decrypts message and writes it to ./me/decrypted.txt
        with open(f'./me/decrypted.txt', 'w') as f:
            f.write(readFromFileAndDecrypt(encrypted_file, './me/keys/vsp_privkey.txt'))

        # if succeeded then print it was a success
        print(f'Successfully decrypted message at /me/decrypted.txt')
        return

    elif os.path.exists(f'./users/{user}'):
        encrypted_file = f'./users/{user}/encrypted.txt'
        
        # decrypts message and writes it to ./users/(user)/decrypted.txt
        with open(f'./users/{user}/decrypted.txt', 'w') as f:
            f.write(readFromFileAndDecrypt(encrypted_file, './me/keys/vsp_privkey.txt'))

        # if succeeded then print it was a success
        print(f'Successfully decrypted message at /users/{user}/decrypted.txt')

    else:
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


def _help():
    """Displays this message."""

    print(f"""encrypt - {encrypt.__doc__}
decrypt - {decrypt.__doc__}
newusr - {newusr.__doc__}
rmusr - {rmusr.__doc__}
help - {_help.__doc__}
-- ADVANCED --
""")


