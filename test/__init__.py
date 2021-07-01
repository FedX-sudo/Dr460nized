#!/usr/bin/env python3
from dntos import shell

print("this is a testing envirornment")

def ls_test():
    print("running ls")
    print(shell.ls('',''))
    if(shell.ls('','')) == "['/Desktop']":
        print("Test Passed! \n\n")
    else:
        print("Test Failed. \n\n")

    print("running ls -l /home")
    print(shell.ls('-l', '/home'))
    if(shell.ls('-l', '/home') == "/Muffin-Man"):
        print("Test Passed! \n\n")
    else:
        print("Test Failed. \n\n")

    print("running ls -a ~")
    print(shell.ls('-a', '~'))
    if(shell.ls('-a', '~') == "['/.local', '/.config', '/Desktop']"):
         print("Test passed!")
    else:
        print("Test Failed.")
    print("running ls thisdirdoesnotexist")
    print(shell.ls('','thisdirnotexist'))

    print("running ls -la ~")
    print(shell.ls('-la', '~'))

    print("running ls -ll")
    print(shell.ls('-ll', ''))
