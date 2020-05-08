#! encoding=utf-8

import pytest

@pytest.fixture()
def fix():
    print("fixture")

@pytest.mark.usefixtures("fix")
def test_fix1():
    print("test_fix1")
class TestFixture:
    @pytest.mark.usefixtures("fix")
    def test_fix2(self):
        print("test_fix2")

    @pytest.mark.usefixtures("fix")
    def test_fix3(self):
        print("test_fix3")
if __name__ == '__main__':
    pytest.main(["-s","-v"])