#!/usr/bin/env python3
import logging
import toml
import os

fs = toml.load(os.getcwd() + '/dntos/resources/fs.toml')
logging.info(toml.dumps(fs))

# Defining the ls emulation function. 
def ls(args, dir):
  l = False
  a = False

  if dir == '~':
    dir = '/home/Muffin-Man'
  elif dir == '':
    dir = workingdir
  elif dir == ' ':
    dir = workingdir


  if args.find('-') == 0:
    if args.find('l') != -1:
      l = True
    if args.find('a') != -1:
      a = True

  if dir in fs:
    out = []
    for match in fs:
        if dir in match:
            match = match.replace(dir,'')
            if a:
              out.append(match)

            elif match.replace('.','')==match:
              out.append(match)

    out.remove('')


  else:
    return("Error: no such file or dirrecotry")
  if l:
    tmp = ['']
    for i in range (0, len(out)):
      tmp.append(out[i])
      tmp.append('\n')
    return ''.join(tmp)
  else:
    return out
