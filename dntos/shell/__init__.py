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
            if match.find('/', 2) != -1:
              match = ''
            elif args.find('-') == 0:
              if args.find('a') != -1:
                out.append(match)
            elif match.replace('.','')==match:
              out.append(match)


    out.remove('')


  else:
    out = ("Error: no such file or dirrecotry")
  if args.find('-') == 0:
    if args.find('l', 1) != -1:
      tmp = []
      for i in range (0, len(out)):
        tmp.append(out[i])
        tmp.append('\n')
      out = ''.join(tmp)




  return out
