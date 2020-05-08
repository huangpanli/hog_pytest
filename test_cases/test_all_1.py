#! encoding=gbk
# 用来测试__all__相关使用
from test_cases.all_1 import *
a = A('zhansan','18')
print(a.name,a.age)
func()
a.method_a2()
__func2__()
# method_b2()
# b=B("lisi",1001)
# NameError: name 'B' is not defined
# func1()
# NameError: name 'func1' is not defined 　

