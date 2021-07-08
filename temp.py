import logging
import toml
import os

fs = toml.load(os.getcwd() + '/dntos/resources/fs.toml')
fs = toml.dumps(fs)
workingdir = toml.loads(fs)

print(toml.dumps(fs))
print(workingdir)
