#! encoding=gbk
# 用来测试__all__相关使用
__all__ = ('func', 'A','__func2__',)


class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method_a1(self):
        print("this is method_a1")

    def method_a2(self):
        print("this is method_a2")


class B():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def method_b1(self):
        print("this is method_b1")

    def method_b2(self):
        print("this is method_b2")


def func():
    print("func() is run!")


def func1():
    print("func1() is run!")

def __func2__():
    print("__func2__ is run!")
