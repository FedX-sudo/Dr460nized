#!/usr/bin/env python3
from dntos import shell

print("this is a testing envirornment")

def ls_test():
    print("running ls")
    print(shell.ls('',''))

    print("running ls -l /home")
    print(shell.ls('-l', '/home'))

    print("running ls -a ~")
    print(shell.ls('-a', '~'))

    print("running ls thisdirdoesnotexist")
    print(shell.ls('','thisdirnotexist'))

    print("running ls -la ~")
    print(shell.ls('-la', '~'))
