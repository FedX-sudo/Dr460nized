#!/usr/bin/env python3
import dntos
from dntos import shell
from dntos.shell import commands
from dntos.shell import parse

def exec(args):
  print(args)

  args = args[11:len(args)]
  print(args)
  out = {}

  out["command"] = args[0:(args.find(' '))] # TODO this requires a space after the command so it is recognized, this is not the way shells work.
  args = args[args.find(' '):len(args)]

  out["flags"] = args[args.find('-'):args.find(' ')] # TODO Python is not finding the '-' character
  print(out)
