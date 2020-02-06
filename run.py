from lib.commands import call_command
from lib.files import setup
import os

if not os.path.exists('./me/keys/me_pubkey.txt'):
    setup()
    

while True:
    cmd = input('>>> ').strip()

    if call_command(cmd):
        if type(call_command(cmd)) is str:
            print(call_command(cmd))

        else:
            print(call_command(cmd)())
