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
  path = []
  tempvar = "contents"
  print(args)
  for i in range (0, len(args["flags"])):
    print("yo")
    if args["flags"][i].find("a") != -1:

      tempvar = "contents_hidden"

  if len(args["subcommand"]) == 0:
      path.append(fs["workingdir"])
  out = ""
  for i in range(0, len(path)):
    try:
      out += (fs[path[i]][tempvar])
    except:
      out += "error" + path[i] + "no such file or directory"

  return (out)
