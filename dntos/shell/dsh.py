#!/usr/bin/env python3

def ls(args, dir):
    if os.path.exist(dir):
      print("dir exists")
    else:
      return("Error: no such file or dirrecotry")
