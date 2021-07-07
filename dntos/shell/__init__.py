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
    parsed_content = toml.load(f)

content_parsed = toml.dumps(parsed_content)

workingdir = fs[44:content_parsed.find("\n", 31)]



def pwd ():
  return(wokingdir)

