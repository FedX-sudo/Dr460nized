#!/usr/bin/env python3
import logging # importing the logging module
import toml # importing the toml module
import os # importing the os module.
'''
This is a piece of code which contains the functions to emulate a unix shell. It takes a dictionary as input via the args variable.
The dictionary does not have to contain anything, but some functions do require it, which is why I chose a dictionary as nothing will break if nothing is provided.
This also opens the config.toml as a dictionary called fs. This allows for full unix file system emulation.
'''
with open(os.path.realpath("dntos/shell/config.toml"), "r") as f: # << this is a thing, which does a thing with another thing. <<
    fs = toml.load(f) # This opening the file into the fs variable as a dictionary... or something...

def pwd(args): # This is defining the pwd function as a function which takes args as the input and does... nothing with it!
   tempvar = fs["workingdir"] # this is a temporary variable called tempvar which is equivalent the the working directory as taken from the fs variable.
   tempvar = fs[tempvar] # this is redefining the tempvar as the workingdir from the file system, so that is can print the whole path
   return tempvar["path"] # This is now returing path that the user is currently in
def ls(args): # this is defining the ls function which is a function to list the stuff within directories and stuff.
  print(args["subcommand"]) # TODO Remove this line! <<<<<<<
  if args["subcommand"] == []: # This is attempting to determine weather the user is wishing to list the contents of the working directory by not providing a path.
# ^^^^^^^^^^^^^^^^^^^^^^ that line does not work for... reasons, therefore I shall make a TODO to fix it.
    path = fs["workingdir"] # This makes the path to list the contents of the working directory
  elif args["path"] == "~": # Determines if the user is wishing to list the contents of /home/Muffin_Man
    path = "Muffin_Man" # Makes the path /home/Muffin_Man
  try: # Attempts to list the path... if it exists
    return("".join(fs["path"])) # Trying to list it.
  except: # If it does not work...
    return("Error, no such file or directory") # Informs the user there is no such file or directory.
