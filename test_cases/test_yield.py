#! encoding=gbk
import pytest
# 函数带yield就是个迭代器
def yield_test(n):
    for i in range(1,n):
        print("i=", i, "迭代")
        yield call(i)
        print("*"*20)
        print("yield后：",i)
        # 做一些其它的事情
    print("do something.")
    print("end.")
def call(i):
    return i * 2
# 使用for循环
for i in yield_test(5):
    print("for循环",i, ",")#此处一定要好好理解i的意思：【什么意思呢，就是yield后面表达式的返回值返回给调用者，并将该返回值作为yield后面的参数传入值使用。就是相当于i = yield call(i)】

# 不带yield
# def yield_test(n):
#     for i in range(n):
#         print("i=", i,"迭代函数")
#         print(call(i))
#         # 做一些其它的事情
#     print("do something.")
#     print("end.")
# def call(i):
#     return i * 2
# yield_test(5)

# # 测试x值是否有变化
# x = 3
# def hello(x):
#     return x*2
# print(hello(x))
# print(x)