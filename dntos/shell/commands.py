#!/usr/bin/env python3
import logging
import toml
import os

with open(os.path.realpath("dntos/shell/config.toml"), "r") as f:
    fs = toml.load(f)

def pwd(args):
   tempvar = fs["workingdir"]
   tempvar = fs[tempvar]
   return tempvar["path"]
def ls(args):
  print(args["path"])
  if args["path"] == []:
    path = fs["workingdir"]
  elif args["path"] == "~":
    path = "Muffin_Man"
  try:
    return("".join(fs["path"]))
  except:
    return("Error, no such file or directory")
