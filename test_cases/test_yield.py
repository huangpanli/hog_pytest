#! encoding=gbk
import pytest
# ������yield���Ǹ�������
def yield_test(n):
    for i in range(1,n):
        print("i=", i, "����")
        yield call(i)
        print("*"*20)
        print("yield��",i)
        # ��һЩ����������
    print("do something.")
    print("end.")
def call(i):
    return i * 2
# ʹ��forѭ��
for i in yield_test(5):
    print("forѭ��",i, ",")#�˴�һ��Ҫ�ú����i����˼����ʲô��˼�أ�����yield������ʽ�ķ���ֵ���ظ������ߣ������÷���ֵ��Ϊyield����Ĳ�������ֵʹ�á������൱��i = yield call(i)��

# ����yield
# def yield_test(n):
#     for i in range(n):
#         print("i=", i,"��������")
#         print(call(i))
#         # ��һЩ����������
#     print("do something.")
#     print("end.")
# def call(i):
#     return i * 2
# yield_test(5)

# # ����xֵ�Ƿ��б仯
# x = 3
# def hello(x):
#     return x*2
# print(hello(x))
# print(x)