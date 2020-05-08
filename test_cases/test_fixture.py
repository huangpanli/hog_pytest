import pytest
import conftest

# @pytest.fixture()
# def login():
#     print("this is login fixture")


def test_case_fix1(login):
    print("want to login fixture"+"test_case_fix1")

def test_case_fix2():
    print("not want to login fixture"+"test_case_fix2")

def test_case_fix3(login):
    print("want to login fixture"+"test_case_fix3")

if __name__ == '__main__':
    pytest.main(["-v","-s"])