#! encoding=gbk
import pytest


@pytest.mark.webtest
def test_web_a():
    print("this is web_a test")


@pytest.mark.webtest
def test_web_b():
    print("this is web_b test")


@pytest.mark.apptest
def test_app_c():
    print("this is app_c test")


@pytest.mark.apptest
def test_app_d():
    print("this is app_d test")

if __name__ == '__main__':
   pytest.main(["-v","-s","-m","webtest"])