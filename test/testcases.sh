#!/bin/sh -e

cd "$(dirname "$0")/.."
strace -o test/log ./dntos.py || echo "test failed, see log for more detail."

#TestCase1: Shell Scripting API

strace -o test/shell.log python3 shell.py || echo "text failed, see log for more details."
