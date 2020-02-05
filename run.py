from lib.commands import call_command


while True:
    cmd = input('>>> ').strip()

    if call_command(cmd):
        if type(call_command(cmd)) is str:
            print(call_command(cmd))

        else:
            print(call_command(cmd)())
