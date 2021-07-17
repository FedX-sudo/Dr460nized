#!/usr/bin/env python3
import dntos # importing the dntos module
from dntos import shell # from within the dntos module it is now importing the shell module
from dntos.shell import commands # from within dntos's shell module it is now importing the commands module
'''
This is the main part of the terminal emulation API, the way it works is you execute shell.exec(args) where args are the command, sub-commands and flags.
Then it goes and parses the command into a dictionary which the functions in commands.py can better understand.
Then it attempts to execute the given command, the first item given in the args, and if it does not exist, it will return "Error command not found"
'''

def exec(args): #defining the exec command which takes args as the input args being any string and it will *hopefully* return a graceful error if it is a bad argument.


  args = args[11:len(args)] # removing the muffin-man> shell prompt

  out = {} # defining the dictionary to port into the command's input
  out["command"] = [] # the command name, this is most assuredly required, and on top of that is the only required part of the dictionary
  out["flags"] = [] # the command's flags. See Bash flags for more details.
  out["subcommand"] = [] # this is a catchall for additional sub-commands to be executed, optional.
  args = args.split(" ") # splitting the args variable into an array.
  for i in range(0, len(args)): # this is a loop to append the out
    print(len(args))
    if i == 0: # this is determining weather the for loop variable is equal to zero.
      out["command"] = args[0] # this line and the last line are used to determine the what the command is, which will always be the first command.
    elif args[i].find("--") != -1: # this is finding flags marked with two dashes IE exa --icons
      out["flags"].append(args[i]) # this appends the out dictionary with the previously found flag.
    elif args[i].find("-") != -1: # This finds flags with a single dash I.E. la -l
      out["flags"].append(args[i]) # This appends the dictionary with the previously found flag
    else: # In case something  else is in the i position of the array which was not previously checked.
      out["subcommand"].append(args[i]) # appending the dictionary with the previously found thing

  try:
    method_to_call = getattr(commands, out["command"]) # This is attempting to execute the shell command
    return(method_to_call(out))
  except:
    return("Error command not found")
