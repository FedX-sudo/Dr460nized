#!/usr/bin/env python3
import dntos
from dntos import shell
from dntos.shell import commands
from dntos.shell import parse

def exec(args):


  args = args[11:len(args)]

  out = {}
  out["command"] = []
  out["flags"] = []
  out["path"] = []
  out["subcommand"] = []
  args = args.split(" ")

  for i in range(0, len(args)):
    if i == 0:
      out["command"] = args[0]
    elif args[i].find("--") != -1:
      out["flags"].append(args[i])
    elif args[i].find("/") != -1:
      out["path"].append(args[i])
    elif args[i].find("-") != -1:
      out["flags"].append(args[i])
    else:
      out["subcommand"].append(args[i])


  try:
    method_to_call = getattr(commands, out["command"])
    return(method_to_call(out))
  except:
    return("Error command not found")
