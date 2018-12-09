#  http://blog.thedigitalcatonline.com/blog/2016/03/06/python-mocks-a-gentle-introduction-part-1/
import mock
import pytest
from mock import patch
from functions_to_test_using_mock_or_monkey import (
    func,
    func_get,
    execute_operations
)


def test_dico():
    d = dict()
    d[1] = "un"
    d["un"] = 1
    d[2] = "deux"
    assert d[1] == "un"
    assert d[2] == "deux"
    assert d["un"] == 1


@pytest.mark.parametrize("p, res", [
    ("premier path", "done"),
    ("deuxieme path", "done")
])
def test_monkey(monkeypatch, p, res):
    import os

    def mock_chdir(d):
        print("mocking chdir to {}".format(d))

    monkeypatch.setattr(os, "chdir", mock_chdir)

    rc = func(p)
    assert rc == res


# Here we are mocking os.chdir with monkeypatch whereas below we are using mock.patch
def test_stuff(monkeypatch):
    import os
    monkeypatch.setattr(os, "chdir", lambda x: None)
    func("new path")


# Here we are mocking os.chdir using mock.patch
@patch("os.chdir")
def test_func(chdir_mock):
    rc = func("to this new dir")
    chdir_mock.assert_called_with("to this new dir")
    assert rc == "done"


# in this example the obect to mock is hard coded in the library as opposed to injected
# the object is only patched within the with statement
def test_func_get_with_patch_form():
    with patch("os.getcwd") as getcwd_mock:
        getcwd_mock.return_value = "some dir"
        rc = func_get()
        getcwd_mock.assert_called_with()
        assert rc == 'some dir'


# the object is patched within the entire test case
@patch("os.getcwd")
def test_mock_using_patch_decorator(getcwd_mock):
    getcwd_mock.return_value = "/some/path"
    rc = func_get()
    getcwd_mock.assert_called_with()
    assert rc == "/some/path"


#  in this case the object is injected therefore we can use the mock object which
# as the particularity to tag along any new attribute read or assigned or called
# so the operation add and sub can be tester "on the fly"
def test_execute_operations():
    operation_mock = mock.Mock()
    operation_mock.add.return_value = 123
    rc = execute_operations(operation_mock, 5, 3)
    assert rc == 123
    operation_mock.sub.assert_called_with(5, 3)
