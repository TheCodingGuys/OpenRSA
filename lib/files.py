from .keys import makeKeyFiles
import time


def mkfile(path):
    """Makes a file in the specified path."""

    with open(path, 'w'):
        pass


def setup():
    """If the user ran run.py for the first time call this command."""

    print('Setting everything up...\n')
    
    # wait 7 miliseconds to make it look cool, lol
    time.sleep(0.7)

    print('Press enter if default, default is 1024.')
    key_size = input('Encryption and decryption key size: ')

    # if the user didn't specify a key size just use the default
    if not key_size:
        key_size = 1024

    # makes key files
    makeKeyFiles('./me/keys/me', int(key_size))
