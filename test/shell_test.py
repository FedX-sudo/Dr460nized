import pytest
import dntos_test
import dntos.shell



@pytest.fixture
def test_ls_1():
  testvar = shell.ls("","")
  assert testvar.find("/Desktop") == -1,"test failed"
  assert testvar.find(".local") != -1, "test failed"
