import pytest
from dntos import shell

testvar = shell.ls("","")
assert testvar.find("Desktop") == -1,"test failed"
assert testvar.find(".local") != -1, "test failed"
