#! encoding=gbk
# 主要用来练习setup和teardown相关方法
import pytest
def setup_module():
    print("该模块下所有测试用例执行开始前执行一次")
def teardown_module():
    print("该模块下所有测试用例执行最后结束时执行一次")
def setup_function():
    print("该模块下每个函数测试用例执行开始前执行一次")
def teardown_function():
    print("该模块下每个函数测试用例执行最后结束时执行一次")
def test_func1():
    print("this is func1")
def test_func2():
    print("this is func2")
def test_func3():
    print("this is func3")

class TestDemo2:
    def setup_class(self):
        print("类开始前执行一次")
    def teardown_class(self):
        print("类最后结束时执行一次")

    def setup_method(self):
        print("类中每个方法开始前执行一次"+"setup_method")
    def teardown_method(self):
        print("类中每个方法最后结束时执行一次"+"setup_method")

    def setup(self):
        print("类中每个方法开始前执行一次"+"setup")
    def teardown(self):
        print("类中每个方法最后结束时执行一次"+"teardown")

    def test_print1(self):
        print("this is test_print1")
    def test_print2(self):
        print("this is test_print2")
    def test_print3(self):
        print("this is test_print3")
if __name__ == '__main__':
    pytest.main(["-v","-s"])