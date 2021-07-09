#!/usr/bin/env python3
import logging
import toml
import os

with open("/home/fedx/Desktop/Code/Dr460nized/dntos/shell/config.toml", "r") as f:
    fs = toml.load(f)

def pwd(args):
  return fs["workingdir"]
