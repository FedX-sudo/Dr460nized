#!/usr/bin/env python3
import dntos.shell.commands

def parse_command(args):
    out = {
      "command" : commands.ls,
      "args": ["l","a"],
      "path": "/home/Muffin_Man/"
    }
    return(out)
