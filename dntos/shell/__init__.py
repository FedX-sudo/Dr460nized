#!/usr/bin/env python3
import dntos
from dntos import shell
from dntos.shell import commands
from dntos.shell import parse

def exec(args):
  args = parse.parse_command(args)

  command = args["command"]
  try:
    commands.command(args)
  except:
    return "Error command not found."
