#! encoding=gbk
import pytest

@pytest.mark.webtest
def test_web1():
    print("this is web1 test")

@pytest.mark.webtest
def test_web2():
    print("this is web2 test")


@pytest.mark.apptest
def test_app1():
    print("this is app1 test")


@pytest.mark.apptest
def test_app2():
    print("this is app2 test")


if __name__ == '__main__':
   pytest.main(["-v","-s","-m","webtest"])