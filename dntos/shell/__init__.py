#!/usr/bin/env python3
import logging
import toml
import os

class Content(object):
  def __init__ (self, path, privlaged, hidden, obj_type, contents):
    self.path = path
    self.privlaged = privlaged
    self.hidden = hidden
    self.obj_type = obj_type
    self.contents = contents


with open("/home/fedx/Desktop/Code/Dr460nized/dntos/shell/config.toml", "r") as f:
    fs = toml.load(f)

def pwd():
  tempvar = ["workingdir"]
  return tempvar["path"]

def ls(flags, path):
  if path == "":
    path = fs["workingdir"]
  elif path == " ":
    path = fs["workingdir"]

  try:
    fs[path]
  except:
    return("ERROR: No such file or dirrectory")

  tempvar = fs[path]
  if tempvar["type"] == "file":
    return tempvar["name"]

  elif (flags.find("-") != -1):
    if (flags.find("a") != -1):
      return tempvar["contents_hidden"]

  else:
    return tempvar["contents"]



