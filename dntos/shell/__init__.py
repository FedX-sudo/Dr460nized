#!/usr/bin/env python3
import dntos
from dntos import shell
from dntos.shell import commands
from dntos.shell import parse

def exec(args):


  args = args[11:len(args)]

  out = {}

  out["command"] = args[0:(args.find(' '))] # TODO this requires a space after the command so it is recognized, this is not the way shells work.
  args = args[args.find(' '):len(args)]
  out["flags"] = []
  while args.find("--") != -1: #major face palm moment here, I forgot to remove the flag from the args variable...
    out["flags"].append(args[args.find("--"):args.find(" ")])

    args = args[args.find("--"):args.find(" ", args.find("--"))]

  print(out)
