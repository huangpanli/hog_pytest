#! encoding=gbk
# ��Ҫ������ϰsetup��teardown��ط���
import pytest
def setup_module():
    print("��ģ�������в�������ִ�п�ʼǰִ��һ��")
def teardown_module():
    print("��ģ�������в�������ִ��������ʱִ��һ��")
def setup_function():
    print("��ģ����ÿ��������������ִ�п�ʼǰִ��һ��")
def teardown_function():
    print("��ģ����ÿ��������������ִ��������ʱִ��һ��")
def test_func1():
    print("this is func1")
def test_func2():
    print("this is func2")
def test_func3():
    print("this is func3")

class TestDemo2:
    def setup_class(self):
        print("�࿪ʼǰִ��һ��")
    def teardown_class(self):
        print("��������ʱִ��һ��")

    def setup_method(self):
        print("����ÿ��������ʼǰִ��һ��"+"setup_method")
    def teardown_method(self):
        print("����ÿ������������ʱִ��һ��"+"setup_method")

    def setup(self):
        print("����ÿ��������ʼǰִ��һ��"+"setup")
    def teardown(self):
        print("����ÿ������������ʱִ��һ��"+"teardown")

    def test_print1(self):
        print("this is test_print1")
    def test_print2(self):
        print("this is test_print2")
    def test_print3(self):
        print("this is test_print3")
if __name__ == '__main__':
    pytest.main(["-v","-s"])