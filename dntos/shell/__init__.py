#!/usr/bin/env python3
fs = ['/', '/usr', '/home', '/root', '/home/tempuser', '/home/tempuser/.local', '/home/tempuser/.config', '/home/tempuser/Desktop']
workingdir = '/homme/tempuser'

def ls(args, dir):
  if dir == '~':
    dir = '/home/tempuser'

  if dir in fs:
    out = []

    for match in fs:
        if dir in match:
            match = match.replace(dir,'')
            if args.find('a') != 0:
              out.append(match)

            elif match.replace('.','')==match:
              out.append(match)

    out.remove('')


  else:
    out = ("Error: no such file or dirrecotry")

  return out
